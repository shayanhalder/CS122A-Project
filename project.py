import mysql.connector
import sys
from json import dumps
from table_initialization import import_dataset
from base_model_commands import listInternetService, countCustomizedModel, addCustomizedModel, deleteBaseModel, listBaseModelKeyWord
from nl2sql_commands import readNL2SQLresult
from agent_client_commands import insertAgentClient, topNDurationConfig

def main():
	mydb = mysql.connector.connect(
		host="localhost",
		user="test",
		password="password",
	)
	
	mycursor = mydb.cursor()
	mycursor.execute("USE cs122a;")
  
	command = sys.argv[1]
 
	if command == 'import':
		response = import_dataset(sys.argv[2], mycursor, mydb)
		print(response)
	elif command == "insertAgentClient":
		values = sys.argv[2:]
		response = insertAgentClient(values, mycursor, mydb)
		print(response)
	elif command == 'topNDurationConfig':
		uid = sys.argv[2]
		N = sys.argv[3]
		response = topNDurationConfig(mycursor, uid, N)
		for res in response:
			print(res)
	elif command == 'listInternetService':
		id = sys.argv[2]
		response = listInternetService(mycursor, id)
		for res in response:
			print(res)
	elif command == 'listBaseModelKeyWord':
		keyword = sys.argv[2]
		response = listBaseModelKeyWord(mycursor, keyword)
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



