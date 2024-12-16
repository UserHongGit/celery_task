import time

def add(x, y):
    result = x + y
    print(f"Task 'add' executed. Result: {result}")
    return result

def print_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Current time: {current_time}")
