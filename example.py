from time import time, sleep 

def my_function(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        sleep(2)
        end_time = time()  # Simulating a delay
        time_taken = end_time - start_time
        print(f"Time taken: {time_taken} seconds")
        return result
    return wrapper

@my_function
def add(a, b):
    return a + b
result = add(5, 10)
print(f"Result: {result}")