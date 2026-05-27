import json
import os

QUEUE_FILE = "runtime_queue.json"

def load_queue():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_queue(queue):
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)


def add_task(task):
    queue = load_queue()
    queue.append(task)
    save_queue(queue)


def pop_task():
    queue = load_queue()
    if not queue:
        return None
    task = queue.pop(0)
    save_queue(queue)
    return task