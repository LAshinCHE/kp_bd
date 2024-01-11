from app.dataBase.config import host, user, password, db_name
import psycopg2


def get_connection():
    conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
    cur = conn.cursor()

    return conn, cur


def check_version():
    
    conn, cur = get_connection()
    cur.execute(
        "SELECT version();"
    )
    response = cur.fetchone()
    print(f"POSTGRE VERSION:{response}")
    return response

