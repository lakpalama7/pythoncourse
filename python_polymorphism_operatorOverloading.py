
class Student:


    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,others):
        m1=self.m1 + others.m1
        m2=self.m2 + others.m2

        m3= Student(m1,m2)
        return m3
    
    def __gt__(self,others):
        m1=self.m1 + self.m2
        m2=others.m1+others.m2

        if m1 > m2:
            return True
        else:
            return False
        
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2) # f"{self.m1} {self.m2}"

s1=Student(70,70)
s2=Student(50,59)

s3= s1 + s2

print(s3.m1)
print(s3.m2)


if s1>s2:
    print("s1 is greater")
else:
    print("s2 is greater")

print(s1)
print(s2)
print(s3)

print("---"*10)
print(s1.__str__())
print(s2.__str__())

        