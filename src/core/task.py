from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, priority, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.created_at = datetime.utcnow()

    def to_tuple(self):
        return (
            self.title,
            self.description,
            self.due_date,
            self.priority,
            self.status,
            self.created_at
        )