

class Pycharm:

    def execute(self):
        print("Execute the code")
        print("Cleans the code")
        print("Debug the code")

class Editor:
    def execute(self):
        print("Execute the code")
        print("Cleans the code")
        print("Debug the code")
        print("Best execution features")
        print("More features")

class Laptop:

    def code(self,ide):
        ide.execute()  #here we are concern about the types of objects but object must have execute() method 


pyc=Editor()

lap=Laptop()
lap.code(pyc)