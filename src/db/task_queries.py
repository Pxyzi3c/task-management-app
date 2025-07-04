from src.db.db import create_connection

class TaskRepository:
    @staticmethod
    def insert_task(task):
        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                INSERT INTO tasks (title, description, due_date, priority, status, created_at)
                VALUES (%s, %s, %s, %s, %s, %s);
                """
                cursor.execute(query, task.to_tuple())
                conn.commit()
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def fetch_tasks(filter_by=None):
        conn = create_connection()
        tasks = []
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)
                query = "SELECT * FROM tasks"
                if filter_by:
                    conditions = " AND ".join([f"{k}=%s" for k in filter_by])
                    query += f" WHERE {conditions}"
                    cursor.execute(query, list(filter_by.values()))
                else:
                    cursor.execute(query)
                tasks = cursor.fetchall()
            finally:
                cursor.close()
                conn.close()
        return tasks

    @staticmethod
    def update_task(task_id, updates):
        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                updates_sql = ", ".join([f"{k}=%s" for k in updates])
                query = f"UPDATE tasks SET {updates_sql} WHERE id=%s"
                values = list(updates.values()) + [task_id]
                cursor.execute(query, values)
                conn.commit()
            finally:
                cursor.close()
                conn.close()

    @staticmethod
    def delete_task(task_id):
        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM tasks WHERE id=%s"
                cursor.execute(query, (task_id,))
                conn.commit()
            finally:
                cursor.close()
                conn.close()