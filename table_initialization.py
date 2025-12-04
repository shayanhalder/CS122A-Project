

def get_query(file_path: str):
    with open(f"sql/{file_path}.sql", 'r') as f:
        sql_script = f.read()
    return sql_script


def create_tables(cursor):
    # must create tables in specific order due to foreign key constraints and dependencies
    sql_file_paths = ['User', 'AgentCreator', 'AgentClient', 'BaseModel', 'CustomizedModel', 
                      'Configuration', 'InternetService', 'LLMService', 'DataStorage', 'ModelServices', 
                      'ModelConfigurations'] 
    
    cursor.execute("DROP DATABASE IF EXISTS AgentPlatform;")
    cursor.execute("CREATE DATABASE AgentPlatform;")
    cursor.execute("USE AgentPlatform;")
    
    for file_path in sql_file_paths:
        sql = get_query(file_path)
        cursor.execute(sql)
    
# def load_csv_data(csv_file_path: str, cursor, table_name: str, csv_file_path: str):
#     load_data_query = f"""
#     LOAD DATA LOCAL INFILE '{csv_file_path}'
#     INTO TABLE {table_name}
#     FIELDS TERMINATED BY ','
#     ENCLOSED BY '"'
#     LINES TERMINATED BY '\n'
#     IGNORE 1 ROWS;
#     """
#     cursor.execute(load_data_query)
    
