# tasks/test_task.py
from base_config import app
import time


@app.task
def add_item():
    try:
        print(f"Item  added successfully")
        return "okokokokokok"
    except Exception as e:
        print(f"Task failed with error: {str(e)}")
        raise e  # Re-raise the exception to ensure task failure is logged


@app.task
def add(x, y):
    return x + y

@app.task
def print_time():
    print(f"Current time: {time.strftime('%Y-%m-%d %H:%M:%S')}")