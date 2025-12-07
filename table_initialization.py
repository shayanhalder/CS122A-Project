def get_query(file_path: str) -> str:
    with open(f"sql/{file_path}.sql", 'r') as f:
        sql_script = f.read()
    return sql_script


def create_tables(cursor, mydb) -> str:
    # must create tables in specific order due to foreign key constraints and dependencies
    try: 
        sql_file_paths = ['User', 'AgentCreator', 'AgentClient', 'BaseModel', 'CustomizedModel', 
                            'Configuration', 'InternetService', 'LLMService', 'DataStorage', 'ModelServices', 
                            'ModelConfigurations'] 

        cursor.execute("DROP DATABASE IF EXISTS AgentPlatform;")
        cursor.execute("CREATE DATABASE AgentPlatform;")
        cursor.execute("USE AgentPlatform;")

        for file_path in sql_file_paths:
            sql = get_query(file_path)
            cursor.execute(sql)
            mydb.commit()
        return "Success"
    except Exception: 
        return "Fail"
        
def load_csv_data_file(csv_file_path: str, cursor, mydb) -> str:
    try: 
        with open(csv_file_path, 'r') as f:
            csv_data = f.read()
            
        lines = csv_data.splitlines()
        for line in lines[1:]:  # skip header
            values = line.split(',')
            for i, value in enumerate(values):
                if any(c.isalpha() or c == '-' for c in value):
                    values[i] = "\'" + value + "\'"
                    
            formatted_values = ', '.join(values)
            
            load_data_query = f"""
            INSERT INTO {csv_file_path.split('/')[1].split('.')[0]} ({(lines[0])})
            VALUES ({formatted_values});
            """
            cursor.execute(load_data_query)
            mydb.commit()
        return "Success"
    except Exception: 
        return "Fail"
    
def load_csv_data(cursor, mydb, csv_dir: str) -> str:
    csv_files = ['User.csv', 'AgentCreator.csv', 'AgentClient.csv', 'BaseModel.csv', 
                'CustomizedModel.csv', 'Configuration.csv', 'InternetService.csv', 
                'LLMService.csv', 'DataStorage.csv', 'ModelServices.csv', 
                'ModelConfigurations.csv']
    # need to load in specific order due to foreign key constraints
        
    for csv_file in csv_files:
        response = load_csv_data_file(f"{csv_dir}/{csv_file}", cursor, mydb)
        if response == "Fail":
            return "Fail"
    return "Success"

def import_dataset(folder_name: str, cursor, mydb) -> str:
    response1 = create_tables(cursor, mydb)	
    if response1 == "Fail":
        return "Fail"
    response2 = load_csv_data(cursor, mydb, folder_name)
    if response2 == "Fail":
        return "Fail"
    return "Success"