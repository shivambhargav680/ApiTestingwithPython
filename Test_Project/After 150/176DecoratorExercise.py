from functools import wraps
import time

def Calculate_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'{function.__name__}')
        t1 = time.time()
        return_value = function(*args, **kwargs)
        t2 = time.time()
        total_time = t2-t1
        print(total_time)
        return return_value
    return wrapper

@Calculate_time
def square(n):
    return [i**2 for i in range(1,n+1)]
square(100000)