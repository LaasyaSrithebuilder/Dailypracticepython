# def myfunction(myparameter: int):
#    # pass # type: can be any while  cmd line comment
#     print(myparameter)

# myfunction(10)  # Calling the function with a string argument
#Still returns the output because python is dynamically typed language and type hints are not enforced at runtime.
#to check it use a type checker like mypy

def myfunction(myparameter: int) -> str:
    return str(myparameter)
#if types are different it shows error

def otherfunction(otherparameter: str):
    print(otherparameter)
otherfunction(myfunction(10))  # This works fine as myfunction returns a string