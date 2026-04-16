Scenario 2: Logging Decorator
Python
import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func._name_} executed in {end - start:.6f} seconds")
        return result
    return wrapper

@log_execution_time
def calculate_sum(n):
    return sum(range(1, n+1))
