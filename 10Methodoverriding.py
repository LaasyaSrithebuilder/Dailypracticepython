class A:
    def display(self):
        return "Method from class A"

# class B:
#     def display(self):
#         return "Method from class B" 

class B(A):
    pass 
    
a = A()
b = B()
print(a.display())  # Output: Method from class A
print(b.display())  # Output: Method from class B