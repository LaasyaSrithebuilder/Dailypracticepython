def logged(func):

    def wrapper(*args, **kwargs): # variable arguments named and unnamed
        result = func(*args, **kwargs)
        with open("log.txt", "a+") as f:
            name = func.__name__
            print(f"Function '{name}' returned value {result}")
            f.write(f"Function '{name}' returned value {result}\n")
        return result   
    return wrapper
@logged    
def add(a, b):
    return a + b

print(add(10,15))