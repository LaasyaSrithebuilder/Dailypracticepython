class Laptop:
    def code(self,ide):
        ide.run()
class Pycharm:
    def run(self):
        print("Running in Pycharm") 
        
class VSCode:
    def run(self):
        print("Running in VSCode")

ide = VSCode() # Duck typing: any object with a run() method can be used here
#ide = Pycharm() # Changing the ide to another class with run() method can be changed the typre of ide
lap1 = Laptop()
lap1.code(ide)