from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import time 
from pydantic import BaseModel, Field, HttpUrl
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
    original_url: HttpUrl

class ShortenURLResponse(BaseModel):
    original_url: HttpUrl
    code: str
    shortened_url: HttpUrl

# Storage dict 
secrets_db = {} # code to url
logging_db = {} # code to list of click records

def generate_short_code(original_url: HttpUrl):
    """Takes a URL and gives a secret code"""
    for code, url in secrets_db.items():
        if original_url == url:
            return code
    secret_code = secrets.token_urlsafe(6)
    secrets_db[secret_code] = original_url
    return secret_code

@app.post("/shorten")
@timer
def shorten_url(request: ShortenURLRequest):
    original_url = request.original_url
    secret_code = generate_short_code(original_url)
    shortened_url = f"http://localhost:8000/{secret_code}"
    return ShortenURLResponse(
        original_url=original_url,
        code=secret_code,
        shortened_url=shortened_url
    )


@app.get("/{code}")
@timer
def redirect_to_new(code: str):
    if not code in secrets_db: 
        raise HTTPException(status_code=404, detail="Not found in DB")
    else: 
        # Log the click
        if code not in logging_db:
            logging_db[code] = []
        logging_db[code].append(datetime.now())
        return RedirectResponse(secrets_db[code])



