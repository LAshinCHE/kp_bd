from app.dataBase.db import get_connection
from app.schemas.orders import Orders


def get_orders_db():
    conn, cur = get_connection()
    request = cur.mogrify("""SELECT * FROM orders""")
    cur.execute(request)
    response = cur.fetchall()
    return response

def get_user_orders(user_id : int):
    conn, cur = get_connection()
    request = cur.mogrify("""SELECT * FROM orders WHERE client_id = %s""", (user_id,))
    cur.execute(request)
    response = cur.fetchall()
    return response

def delete_order_db(order_id: int):
    conn, cur = get_connection()
    request = cur.mogrify("""DELETE FROM order_products WHERE order_id = %s""", (order_id,)) 
    cur.execute(request)
    conn.commit() 
    request = cur.mogrify("""DELETE FROM orders WHERE id = %s""", (order_id,)) 
    cur.execute(request)
    conn.commit() 


def make_order(order: Orders):
    conn, cur = get_connection()
    request = cur.mogrify("""INSERT INTO orders (id, order_number, order_date, order_status, order_delivery, client_id)
                        VALUES ( %s, %s, %s, %s, %s, %s)
                          """, (order.id,
                                order.order_number, 
                                order.order_date, 
                                order.order_status,
                                order.order_delivery,
                                order.client_id
                                ))
    cur.execute(request)
    conn.commit()    


def take_max_id():
    conn, cur = get_connection()
    request = cur.mogrify("""SELECT MAX(id) FROM orders""")
    cur.execute(request)
    response = cur.fetchall()
    return response