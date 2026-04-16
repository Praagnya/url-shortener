from fastapi import FastAPI
import time 
from functools import wraps

app = FastAPI()

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper


