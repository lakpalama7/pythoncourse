
class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.lab=self.Laptop() #Innerclass object created inside the outerclass.

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")
        self.lab.show()

    class Laptop:
        def __init__(self):
            self.brand='Hp'
            self.cpu='i5'
            self.ram='8GB'

        def show(self):
            print(f"Brand : {self.brand}, CPU: {self.cpu}, RAM: {self.ram}")



s1=Student('lakpa',20)
s2=Student('hari',10)

s1.show()
s2.show()

# lap1=Student.Laptop()  #Creating Inner class object outside the OuterClass -- only Using Outerclass Innerclass obj can be created.
# print(lap1.brand)

