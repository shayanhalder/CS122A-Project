import mysql.connector
import sys
from dotenv import dotenv_values, load_dotenv
from table_initialization import import_dataset
from base_model_commands import listInternetService, countCustomizedModel, addCustomizedModel, deleteBaseModel
from agent_client_commands import insertAgentClient

load_dotenv()
config = dotenv_values(".env")

def main():
	print(sys.argv)
    
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
		response = import_dataset(sys.argv[2], mycursor, mydb)
		print(response)
	elif command == "insertAgentClient":
		values = sys.argv[2:]
		response = insertAgentClient(values, mycursor, mydb)
		print(response)
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
	
    
if __name__ == "__main__":
    main()



