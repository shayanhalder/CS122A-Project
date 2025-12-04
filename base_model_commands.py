def listInternetService(cursor, id):
    cursor.execute(f'''SELECT s.sid, s.endpoints, s.provider
                   FROM InternetService AS s JOIN ModelServices AS ms ON s.sid = ms.sid
                   WHERE ms.bmid = {id}
                   ORDER BY s.provider ASC''')
    
    response = cursor.fetchall()
    
    for i in range(len(response)):
        res = response[i]
        response[i] = f'{res[0]},{res[1]},{res[2]}'

    if len(response) == 0:
        response = ["Invalid input, values not found."]

    return response

def countCustomizedModel(cursor, ids):
    pass