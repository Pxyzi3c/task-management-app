import logging

from src.db.mongo_client import tasks_collection
from src.utils.logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

class TaskManager:
    def add_task(self, task):
        try:
            tasks_collection.insert_one(task.to_dict())
            logger.info("Task added successfully.")
        except Exception as e:
            logger.error(f"Failed to add task: {e}")

    def list_tasks(self, filter_by=None):
        query = filter_by if filter_by else {}
        return list(tasks_collection.find(query))

    def update_task(self, task_id, updates):
        tasks_collection.update_one({"_id": task_id}, {"$set": updates})

    def mark_complete(self, task_id):
        self.update_task(task_id, {"status": "Completed"})

    def delete_task(self, task_id):
        tasks_collection.delete_one({"_id": task_id})