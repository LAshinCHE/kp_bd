from app.dataBase.db import get_connection


def get_category_db():
    conn, cur = get_connection()
    request = cur.mogrify("""SELECT * FROM category""")
    cur.execute(request)
    response = cur.fetchall()
    return response
