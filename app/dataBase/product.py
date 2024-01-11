from app.dataBase.db import get_connection

def get_products_db():
    conn, cur = get_connection()
    request = cur.mogrify("""SELECT * FROM products""")
    cur.execute(request)
    response = cur.fetchall()
    return response