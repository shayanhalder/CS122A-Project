import mysql.connector
import sys
from json import dumps
from dotenv import dotenv_values, load_dotenv
from table_initialization import create_tables, load_csv_data
from base_model_commands import listInternetService, countCustomizedModel, addCustomizedModel, deleteBaseModel
from nl2sql_commands import readNL2SQLresult

load_dotenv()
config = dotenv_values(".env")

def main():
	print("Command-line args: ", sys.argv, '\n')
    
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password=config["PASSWORD"],
  		database="AgentPlatform"
	)
 
	print("Connection successful\n")

	mycursor = mydb.cursor()
	command = sys.argv[1]
 
	if command == 'import':
		create_tables(mycursor, mydb)	
		print("Tables created successfully")
		folder_name = sys.argv[2]
		load_csv_data(mycursor, mydb, folder_name)
		print("Data loaded successfully")
	elif command == 'listInternetService':
		id = sys.argv[2]
		response = listInternetService(mycursor, id)
		for res in response:
			print(res)
	elif command == 'countCustomizedModel':
		pass
		ids = sys.argv[2:]
		response = countCustomizedModel(mycursor, ids)
		for res in response:
			print(res)
	elif command == 'addCustomizedModel':
		mid = sys.argv[2]
		bmid = sys.argv[3]
		response = addCustomizedModel(mycursor, mydb, mid, bmid)
		print(response)
	elif command == 'deleteBaseModel':
		bmid = sys.argv[2]
		response = deleteBaseModel(mycursor, mydb, bmid)
		print(response)
	elif command == 'printNL2SQLresult':
		response = readNL2SQLresult('./NL2SQL.csv')
		for i, res in enumerate(response):
			print("{")
			for key, value in res.items():
				if key == "LLM_returned_SQL_query" or key == "prompt":
					print(f'  "{key}":\n"""\n{value}\n""",')
				else:
					print(f'  "{key}": {dumps(value)},')
			print("}," if i < len(response) - 1 else "}")

if __name__ == "__main__":
    main()



