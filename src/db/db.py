import mysql.connector
from mysql.connector import Error
from config.settings import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

def create_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if conn.is_connected():
            print("✅ MySQL connection successful")
            return conn
    except Error as e:
        print(f"❌ Error: {e}")
    return None