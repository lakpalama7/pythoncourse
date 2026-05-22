from threading import Thread, Lock
from time import sleep
from concurrent.futures import ThreadPoolExecutor

class Counter:
    def __init__(self, lock):
        self.lock = lock
        self.value = 0

    def increment(self, id, value):
        with self.lock:
            current_value = self.value
            current_value += value
            sleep(1)
            self.value = current_value
            print(f"Thread id : {id}, value : {self.value}")



with ThreadPoolExecutor() as executor:
    lock = Lock()
    counter = Counter(lock)
    #for i in range(5):
        #executor.submit(counter.increment, i, 10)
    executor.map(counter.increment, [i for i in range(5)], [1,2,3,4,5,6])