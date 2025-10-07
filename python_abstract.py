from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
        
class Laptop(Computer):
    def process(self):
        print("Laptop is running")

class Desktop(Computer):
    
    def process(self):
        print("Desktop is running")

class Programmer:
    def work(self,obj1,obj2):
        print("Programmer solve bugs")
        obj1.process()
        obj2.process()
        
#com=Computer()
lab=Laptop()
desk=Desktop()
pro=Programmer()
pro.work(lab,desk)

