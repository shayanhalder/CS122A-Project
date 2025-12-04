import mysql.connector
import sys
from dotenv import dotenv_values, load_dotenv
from table_initialization import create_tables

load_dotenv()
config = dotenv_values(".env")

def main():
	print("Command-line args: ", sys.argv)
    
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password=config["PASSWORD"],
  		database="agent_platform"
	)
 
	print("Connection successful")

	mycursor = mydb.cursor()
	create_tables(mycursor)	
 
	print("Tables created successfully")
    
    
if __name__ == "__main__":
    main()



