# main.py
from base_config import app
from tasks.test_task import add_item

if __name__ == "__main__":
    try:
        result = add_item.delay()
        print(f"Task result: {result.get(timeout=10)}")
    except Exception as e:
        print(f"Error: {str(e)}")