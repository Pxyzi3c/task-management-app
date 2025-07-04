# Task Manager CLI Application

A Python-based command-line application to manage daily tasks using a MySQL database. Designed with clean object-oriented architecture, no ORMs, and built for extensibility — ideal for practicing database interaction, input validation, and modular design principles.

---

## Features

- Add a new task
- List all tasks
- Update a task's details
- Mark a task as complete
- Delete a task
- Task attributes:
  - Title
  - Description
  - Due Date
  - Priority (Low, Medium, High)
  - Status (Pending, In Progress, Completed)
  - Timestamped on creation

---

## Tech Stack

- Python 3.10+
- MySQL (via XAMPP/phpMyAdmin)
- `mysql-connector-python`
- CLI-based interface
- No ORMs (raw SQL used)

---

## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

### 2. Set Up a Virtual Environment

```
python -m venv venv
source venv/Scripts/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Set Up MySQL Database via XAMPP

### 5. Run the application

```
python -m src.main
```