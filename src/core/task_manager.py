import logging
from src.db.db import create_connection
from src.utils.logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

class TaskManager:
    def add_task(self, task):
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
                logger.info("✅ Task added successfully.")
            except Exception as e:
                logger.error(f"❌ Failed to add task: {e}")
            finally:
                cursor.close()
                conn.close()

    def list_tasks(self, filter_by=None):
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
            except Exception as e:
                logger.error(f"❌ Failed to list tasks: {e}")
            finally:
                cursor.close()
                conn.close()
        return tasks

    def update_task(self, task_id, updates):
        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                updates_sql = ", ".join([f"{k}=%s" for k in updates])
                query = f"UPDATE tasks SET {updates_sql} WHERE id=%s"
                values = list(updates.values()) + [task_id]
                cursor.execute(query, values)
                conn.commit()
                logger.info(f"✅ Task {task_id} updated.")
            except Exception as e:
                logger.error(f"❌ Failed to update task: {e}")
            finally:
                cursor.close()
                conn.close()

    def mark_complete(self, task_id):
        self.update_task(task_id, {"status": "Completed"})

    def delete_task(self, task_id):
        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM tasks WHERE id=%s"
                cursor.execute(query, (task_id,))
                conn.commit()
                logger.info(f"✅ Task {task_id} deleted.")
            except Exception as e:
                logger.error(f"❌ Failed to delete task: {e}")
            finally:
                cursor.close()
                conn.close()