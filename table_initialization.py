

def get_query(file_path: str):
    with open(f"sql/{file_path}.sql", 'r') as f:
        sql_script = f.read()
    return sql_script


def create_tables(cursor):
    # must create tables in specific order due to foreign key constraints and dependencies
    sql_file_paths = ['user', 'agent_creator', 'agent_client', 'base_model', 'customized_model', 
                      'configuration', 'internet_service', 'llm_service', 'data_storage', 'internet_utilization', 
                      'configuration_utilization'] 
    
    cursor.execute("DROP DATABASE agent_platform;")
    cursor.execute("CREATE DATABASE agent_platform;")
    cursor.execute("USE agent_platform;")
    
    for file_path in sql_file_paths:
        sql = get_query(file_path)
        cursor.execute(sql)
    

    
