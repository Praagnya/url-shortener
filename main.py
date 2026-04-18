from fastapi import FastAPI
import time 
from pydantic import BaseModel, Field
from functools import wraps
from datetime import datetime 

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

class ShortenURLRequest(BaseModel):
    original_url: str 

class ShortenURLResponse(BaseModel):
    original_url: str 
    code: str 
    shortened_url: str
    # created_at: datetime = Field(default_factory = datetime.now) (let us not show this to user)
