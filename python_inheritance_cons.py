
class A:
    def __init__(self):
        print("A init method")

    def feature1(self):
        print("Feature 1-A is working")


class B(A):
    def __init__(self):
        print("Init method in B")
        super().__init__()


    def feature1(self):
        print("Feature 1-B is working")
        super().feature1()


b=B() #object of B() class look for init() method in class B, if not found then it look in parent class A and use its init() method.
b.feature1()

print("==="*10)

class A:
    def __init__(self):
        print("A init method")

    def feature1(self):
        print("Feature 1-A is working")

    def featureA(self):
        print("class A featureA method is called")


class B:
    def __init__(self):
        print("Init method in B")
        super().__init__()


    def feature1(self):
        print("Feature 1-B is working")
        
         

class C(B,A):  #method resolution order (MRO) -- always gets priority to left side class.
    def __init__(self):
        print("Class c init method")
        super().__init__()

    def feature2(self):
       print("class c feature")
       super().feature1() #it calls the method of class B sine B is in left side during C(B,A) inheritance.
       super().featureA()

c=C()
c.feature1() #since A, B has same method feature1() -- c.feature1() calls the method of class B - since B is in left side C(B,A) inheritance class
c.feature2()
