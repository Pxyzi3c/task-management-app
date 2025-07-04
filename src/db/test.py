from src.db.db import create_connection

if __name__ == "__main__":
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        print("Current DB:", cursor.fetchone())
        cursor.close()
        connection.close()