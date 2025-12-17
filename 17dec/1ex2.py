 #example 2 timing
import time

def timed(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"difference is {end_time - start_time}")
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper
@timed
def myfunction(n):
    res = 1
    for i in range(1,n+1):
        res *= i 
    return res
myfunction(1000)