import sys
import json
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path("tasks.json")

USAGE = """\
Usage:  
      python task_cli.py add 'description'
      python task_cli.py update <id> "new description"
      python task_cli.py delete <id>
      python task_cli.py mark-in-progress <id>
      python task_cli.py mark-done <id>
      python task_cli.py list [todo|in-progress|done] 
"""


def _now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_db():
    if not DB_PATH.exists():
        return {"tasks": []}
    try:
        with DB_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if "tasks" not in data or not isinstance(data["tasks"], list):
            return {"tasks": []}
        return data
    except FileNotFoundError:
        return {"tasks": []}


def save_db(data):
    tmp = DB_PATH.with_suffix(".json.tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DB_PATH)


def next_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


def find_tasks(tasks, id_int):
    for t in tasks:
        if t["id"] == id_int:
            return t
    return None


def set_status(task, status):
    task["status"] = status
    task["updatedAt"] = _now_iso()


def main():
    if len(sys.argv) < 2:
        print(USAGE)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == 'add':
        if len(sys.argv) < 3:
            print("Error occurred")
            print(USAGE)
            sys.exit(1)
        description = sys.argv[2]
        db = load_db()
        tasks = db["tasks"]
        new_task = {
            "id": next_id(tasks),
            "description": description,
            "status": "todo",
            "createdAt": _now_iso(),
            "updatedAt": _now_iso(),
        }
        tasks.append(new_task)
        save_db(db)
        print(f"Task added successfully (ID: {new_task['id']})")
        return

    elif cmd == 'update':
        if len(sys.argv) < 4:
            print("Error: need <id> and \"new description\" ")
            print(USAGE);
            sys.exit(1)
        try:
            id_int = int(sys.argv[2])
        except ValueError:
            print("Error: <id> must be an integer")
            sys.exit(1)
        new_desc = sys.argv[3]

        db = load_db()
        task = find_tasks(db["tasks"], id_int)
        if not task:
            print(f"Error: Task <id_int> not found")
            sys.exit(1)
        task["description"] = new_desc
        task["updatedAt"] = _now_iso()
        save_db(db)
        print(f"Task {id_int} updated.")
        return

    elif cmd == 'delete':
        if len(sys.argv) < 3:
            print("Error: need <id> and \"new description\" ")
            sys.exit(1)
        try:
            id_int = int(sys.argv[2])
        except ValueError:
            print("Error: <id> must be an integer")
            sys.exit(1)

        db = load_db()
        before = len(db["tasks"])
        db["tasks"] = [t for t in db["tasks"] if t["id"] != id_int]
        after = len(db["tasks"])
        if before == after:
            print(f"Error: Task <id_int> not found")
            sys.exit(1)
        save_db(db)
        print(f"Task {id_int} deleted.")
        return

    elif cmd == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("Error: needed <id>")
            sys.exit(1)
        try:
            id_int = int(sys.argv[2])
        except ValueError:
            print("Error: <id> must be an integer")
            sys.exit(1)

        db = load_db()
        task = find_tasks(db["tasks"], id_int)
        if not task:
            print(f"Error: Task <id_int> not found")
            sys.exit(1)
        set_status(task, "in-progress")
        save_db(db)
        print(f"Task {id_int} mark-in-progress.")
        return

    elif cmd == 'mark-done':
        if len(sys.argv) < 3:
            print("Error: needed <id>")
            sys.exit(1)
        try:
            id_int = int(sys.argv[2])
        except ValueError:
            print("Error: <id> must be an integer")
            sys.exit(1)

        db = load_db()
        task = find_tasks(db["tasks"], id_int)
        if not task:
            print(f"Error: Task <id_int> not found")
            sys.exit(1)
        set_status(task, "done")
        save_db(db)
        print(f"Task {id_int} marked done.")
        return

    elif cmd == 'list':
        status = sys.argv[2] if len(sys.argv) >= 3 else None
        valid = {None, "todo", "in-progress", "done"}
        if status not in valid:
            print(f"Error: Status must be one of : todo | in-progress | done")
            sys.exit(1)

        db = load_db()
        tasks = db["tasks"]
        if status:
            tasks = [t for t in tasks if t["status"] == status]

        if not tasks:
            print("(No tasks found)")
            return

        for t in sorted(tasks, key=lambda x: (x["status"], x["id"])):
            print(f"[{t['id']}] {t['description']} :: {t['status']}")
        return

    else:
        print(f"Unknown command: {cmd}\n")
        print(USAGE)
        sys.exit(1)


if __name__ == '__main__':
    main()
