
class A:

    def show(self):
        print("A class method")

class B(A):
    # show() method of class A is overiding in class B.
    def show(self):
        print("B class method") 
        #super().show()


b=B()
b.show()