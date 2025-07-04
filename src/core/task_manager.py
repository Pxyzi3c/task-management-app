import logging
from src.db.task_queries import TaskRepository
from src.utils.logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

class TaskManager:
    def add_task(self, task):
        try:
            TaskRepository.insert_task(task)
            logger.info("✅ Task added successfully.")
        except Exception as e:
            logger.error(f"❌ Failed to add task: {e}")

    def list_tasks(self, filter_by=None):
        try:
            return TaskRepository.fetch_tasks(filter_by)
        except Exception as e:
            logger.error(f"❌ Failed to list tasks: {e}")
            return []

    def update_task(self, task_id, updates):
        try:
            TaskRepository.update_task(task_id, updates)
            logger.info(f"✅ Task {task_id} updated.")
        except Exception as e:
            logger.error(f"❌ Failed to update task: {e}")

    def mark_complete(self, task_id):
        self.update_task(task_id, {"status": "Completed"})

    def delete_task(self, task_id):
        try:
            TaskRepository.delete_task(task_id)
            logger.info(f"✅ Task {task_id} deleted.")
        except Exception as e:
            logger.error(f"❌ Failed to delete task: {e}")