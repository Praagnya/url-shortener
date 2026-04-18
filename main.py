from fastapi import FastAPI
import time 
from pydantic import BaseModel, Field
from functools import wraps
from datetime import datetime 
import secrets 


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

# Storage dict 
secrets_db = {}

def generate_short_code(original_url: str):
    """Takes a URL and gives a secret code"""
    for code, url in secrets_db.items():
        if original_url == url:
            return code
    secret_code = secrets.token_urlsafe(6)
    secrets_db[secret_code] = original_url
    return secret_code

@app.post("/shorten")
def shorten_url(request: ShortenURLRequest):
    original_url = request.original_url
    secret_code = generate_short_code(original_url)


