import mysql.connector
import sys
from dotenv import dotenv_values, load_dotenv
from table_initialization import create_tables, load_csv_data
from base_model_commands import listInternetService, countCustomizedModel

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
		# ids = sys.argv[2:]
		# response = countCustomizedModel(mycursor, ids)
		# print(response)
    
    
if __name__ == "__main__":
    main()



