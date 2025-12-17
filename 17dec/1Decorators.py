# def mydecoratoer(func):
#     def wrapper():
#         print("Before the function call.")
#         func()
#         print("After the function call.")
#     return wrapper

# @mydecoratoer
# def say_hello():
#     print("Hello!")

# say_hello()

# with arguments

def mydecorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call.")
        result = func(*args, **kwargs)
        print("After the function call.")
        return result
    return wrapper

@mydecorator # function is decorated here
def greet(name):
    print(f"Hello, {name}!")    

greet("Alice")