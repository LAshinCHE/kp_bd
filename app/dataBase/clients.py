from app.dataBase.db import get_connection
from app.schemas.clients import Clients
from typing import List

def get_client(id: int):
    conn, cur = get_connection()
    request = cur.mogrify("""SELECT * FROM clients WHERE id  = %s;""", (id,))
    cur.execute(request)
    response = cur.fetchall()
    return response

def get_clients_db():
    conn, cur = get_connection()
    request = cur.mogrify("""SELECT * FROM clients""")
    cur.execute(request)
    response = cur.fetchall()
    return response

def post_client(self,client :List[Clients]):
    conn, cur = get_connection()
    request = cur.mogrify("""INSERT INTO clients 
                                    (id, client_name, client_surname, client_phone, client_address)  
                                    VALUES (%s, %s, %s, %s, %s);""", 
                                    (client[0].id, client[0].client_name, client[0].client_surname,client[0].client_phone, client[0].client_addres)
                                )
    cur.execute(request)
    request2 = cur.mogrify("SELECT * FROM clients;")
    cur.execute(request2)
    response = cur.fetchall()
    conn.commit()  
    return response

def change_client(client: Clients):
    conn, cur = get_connection()
    request = cur.mogrify("""UPDATE clients
                        SET
                            client_name = %s,
                            client_surname = %s,
                            client_phone = %s,
                            client_address = %s
                        WHERE id = %s
                          """, (client.client_name, client.client_surname, client.client_phone, client.client_addres,client.id,))
    cur.execute(request)
    conn.commit()    