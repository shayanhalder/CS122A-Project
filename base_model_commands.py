import mysql.connector

def listInternetService(cursor, id):
    cursor.execute(f'''SELECT s.sid, s.endpoints, s.provider
                   FROM InternetService AS s JOIN ModelServices AS ms ON s.sid = ms.sid
                   WHERE ms.bmid = {id}
                   ORDER BY s.provider ASC''')
    
    response = cursor.fetchall()
    
    for i in range(len(response)):
        res = response[i]
        response[i] = f'{res[0]},{res[1]},{res[2]}'

    return response

def countCustomizedModel(cursor, ids):
    conditional = 'c.bmid = ' + ids[0]
    for i in range(1, len(ids)):
        conditional += ' OR c.bmid = ' + ids[i]
        
    cursor.execute(f'''SELECT b.bmid, b.description, COUNT(*)
                   FROM BaseModel AS b
                   JOIN CustomizedModel AS c ON b.bmid = c.bmid
                   WHERE {conditional}
                   GROUP BY b.bmid
                   ORDER BY b.bmid ASC;''')
    
    response = cursor.fetchall()
    
    for i in range(len(response)):
        res = response[i]
        response[i] = f'{res[0]},{res[1]},{res[2]}'

    return response

def addCustomizedModel(cursor, mydb, mid, bmid): 
    try: 
        query = f'''INSERT INTO CustomizedModel (bmid, mid)
                    VALUES ( {mid}, {bmid})'''
        cursor.execute(query)
        mydb.commit()
        return "Success"
    except mysql.connector.Error as err:
        return "Fail"
    
def deleteBaseModel(cursor, mydb, bmid): 
    try: 
        query = f'''DELETE FROM BaseModel
                    WHERE bmid={bmid}'''
        cursor.execute(query)
        mydb.commit()
        return "Success"
    except mysql.connector.Error as err:
        return "Fail"