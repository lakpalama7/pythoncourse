
class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} Speek")

    def walk(self):
        print("Walk fast")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} bark")



def speak(obj):
    obj.speak()


a=Animal("animal")
b=Dog("tommy")


speak(a)
speak(b)


a = ['this ', 'is ', 'a ', 'hello']
b = ['this ', 'is ', 'a ', 'hello']
print(a==b)
print(a is b)