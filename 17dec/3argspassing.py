# def myfunction(*args, **kwargs):
#     # print ("Positional arguments:", args)
#     # print ("Keyword arguments:", kwargs)
#     print(args[0])
#     print(args[1])
#     print(args[2])  
#     print(kwargs["age"])
#     print(kwargs["name"])


# myfunction('hey',True, 2, 3, name="Alice", age=30,word="hi")

# import sys
# import sys 

# # print(sys.argv) # prints all the arguments passed via command line
# filename =  sys.argv[1]
# word = sys.argv[2]  

# with open (filename, 'w+') as f:
#     f.write(word)

import sys, getopt

filename = 'test.txt'
word = 'hello'

opts, args = getopt.getopt(sys.argv[1:], 'f:w:', ['file=', 'word='])

for opt, arg in opts:
    if opt in ('-f', '--file'):
        filename = arg
    elif opt in ('-w', '--word'):
        word = arg

with open (filename, 'w+') as f:
    f.write(word)