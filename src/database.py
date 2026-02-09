import sqlite3

def get_connection():
    conn = sqlite3.connect("delivery_order.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            order_date TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()
