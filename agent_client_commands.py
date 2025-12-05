
def _check_user_exists(uid, username, email, cursor) -> bool:
    query = f'''SELECT COUNT(*) FROM User 
                WHERE uid = {uid} AND username = '{username}' AND email = '{email}' ;'''
    
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0] > 0

def insertAgentClient(values, cursor, mydb) -> str:
    try:
        uid, username, email = values[0], values[1], values[2]
        card_number, card_holder, expiration_date, cvv, zip, interests = values[3], values[4], values[5], values[6], values[7], values[8]
        user_exists = _check_user_exists(uid, username, email, cursor)
        if not user_exists:
            return "Fail"

        query = f'''INSERT INTO AgentClient (uid,interests,cardholder,expire,cardno,cvv,zip)
                    VALUES ( {uid}, '{interests}', '{card_holder}', '{expiration_date}', '{card_number}', '{cvv}', '{zip}' )'''
        
        cursor.execute(query)
        mydb.commit()
        return "Success"
    except Exception:
        return "Fail"
