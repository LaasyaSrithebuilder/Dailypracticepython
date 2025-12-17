# import sys

# def mygenerator(n):
#     """A simple generator that yields numbers from 0 to n-1."""
#     for i in range(n):
#         yield i ** 3

# value = mygenerator(100) # no change in memory usage even for large n
# print(sys.getsizeof(value))  # prints size of generator object in bytes
# # for v in value:
# #     print (v) # prints numbers from 0 to 99 cubed

# print(next(value)) # prints 0
# print(next(value))  # prints 1
# print(next(value))  # prints 8 

#ex2 infinite generator
def infinite_generator():
    """An infinite generator that yields natural numbers starting from 0."""
    n = 1
    while True:
        yield n
        n += 5
val = infinite_generator()
print(next(val))  # prints 1
print(next(val))  # prints 6 ....
 #for continous val 
for v in val:
    print(v)