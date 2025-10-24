# Task Tracker CLI

A "simple-command line tool" written in python to manage and track your tasks - add,delete,update,mark progress, and list them - all stored in a local "tasks.json" file.
This project was built to practice working with the ** filesystem, JSON and CLI argument parsing **

-------
# Features
- Add new tasks with description
- Delete or update existing tasks
- Mark tasks as "todo","in-progress", or "done"
- List all tasks or filter by status
- Persistent storage in "tasks.json" (auto-created if missing)
- No external libraries required-pure Python

--------
# Requirements
- Python 3.8 above
- No external packages needed(use only built-in modules: 'sys','json', 'datetime','pathlib')

--------
# Installation setup
1. "Clone or create the project directory"
 ---bash
  git clone https://github.com/jiafoo/task-tracker-cli.git
  cd task-tracker-cli

2. Run directory with Python
python tack_cli.py <command> [arguments...]

3. Usage

- add a new task
- python task_cli.py add "Buy groceries"



- delete a task
- python task_cli.py delete 1


- change task status
- python task_cli.py mark-in-progress 1
- python task_cli.py mark-done 1


- list task
- python task_cli.py list              # all tasks
- python task_cli.py list todo         # only not done
- python task_cli.py list in-progress  # only in-progress
- python task_cli.py list done         # only done

# Task Data Format
{
-  "id": 1,
-  "description": "Buy groceries",
-  "status": "todo",
-  "createdAt": "2025-10-24T05:20:32.918Z",
- "updatedAt": "2025-10-24T05:20:32.918Z"  
}

# Project Structure
- task-tracker-cli/
- │
- ├── task_cli.py      # main CLI program
- ├── tasks.json       # created automatically
- └── README.md        # documentation

# Testing
- python task_cli.py add "Read a book"
- python task_cli.py add "Do workout"
- python task_cli.py list
- python task_cli.py mark-in-progress 1
- python task_cli.py mark-done 1
- python task_cli.py update 2 "Do workout for 30 minutes"
- python task_cli.py delete 1
- python task_cli.py list done

# Learning Objectives
This project demonstrates how to:
- Build a command-line interface (CLI) in Python
- Work with the filesystem and JSON persistence
- Handle user inputs and errors gracefully
- Design clean, reusable helper functions

# License
### ✍️ tips when you write yours

1. **Show one-liners first** — users like examples before theory.  
2. **Explain “why”** you built it (“to learn how to handle CLI args and JSON persistence”).  
3. **Keep consistent markdown headings** (`##`, `###`, etc.).  
4. **Avoid copying everything** — describe your own thoughts, like what you learned or what was tricky.  
5. **Optional**: add a short “Demo” section with sample outputs or a gif if you run it in your terminal.

---
