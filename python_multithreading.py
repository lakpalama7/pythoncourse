from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
         print("Hello")
         sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
         print("Hi")
         sleep(1)

hello=Hello()
hi=Hi()

hello.start()
sleep(0.5)
hi.start()

hello.join()
hi.join()
print("main thread")