class Student:
    school = "white house" #class variable or static variable

    def __init__(self):
        self.name="lakpa"
        self.age=30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
    
    def display(self):
        print(f"Name: {self.name} Age: {self.age}")

    @classmethod
    def schoolinfo(cls):
        return cls.school
    
    @staticmethod
    def getInfo():
        print("This is student class...in the best module !!!")


com1=Student()
com1.age=40
com2=Student()

print(com1==com2)
print(com1 is com2)

com1.display()
com2.display()

print(Student.schoolinfo())
Student.getInfo()

if com1.compare(com2):
    print("They are same")

else:
    print("They are different")
