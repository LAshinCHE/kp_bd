from app.dataBase.db import get_connection

def get_order_product_db():
    conn, cur = get_connection()
    request = cur.mogrify("""SELECT * FROM order_products""")
    cur.execute(request)
    response = cur.fetchall()
    return response


def make_order_and_products(product_id: int, order_id : int):
    conn, cur = get_connection()
    request = cur.mogrify("""INSERT INTO order_products (product_id, order_id)
                                VALUES ( %s, %s)""",(product_id, order_id))
    cur.execute(request)
    conn.commit()
