from app.dataBase.db import get_connection

def check_user(user_name : str,user_password : str):
    conn, cur = get_connection()
    request = cur.mogrify("""SELECT * FROM users WHERE user_name = %s AND user_password = %s""",(user_name, user_password,))
    cur.execute(request)
    response = cur.fetchall()
    conn.commit() 
    if response == None:
        return None
    return response


def add_new_user(user_name : str,user_email : str,user_password : str):
    conn, cur = get_connection()
    request = cur.mogrify("""INSERT INTO users 
                                    (user_name, user_password, user_email, user_permission)  
                                    VALUES (%s, %s, %s, 'пользователь')
                            RETURNING id""", 
                                    (user_name, user_password, user_email)
                                )
    cur.execute(request)
    response = cur.fetchall()
    conn.commit()  
    return response

def get_user(user_name : str,user_password : str):
    conn, cur = get_connection()
    request = cur.mogrify("""SELECT id FROM users WHERE user_name  = %s AND user_password = %s""", 
                                    (user_name, user_password)
                                )
    cur.execute(request)
    response = cur.fetchall()
    conn.commit()  
    return response

