
from time import sleep
from threading import Lock, Thread


class Counter:
    def __init__(self,lock):
        self.value=0
        self.lock=lock

    def increment(self, val):
        with self.lock:
            counter_value = self.value
            counter_value += val

            sleep(1)

            self.value = counter_value
            print(f"Counter value is : {self.value}")

lock=Lock()
counter = Counter(lock)
t1 = Thread(target=counter.increment, args=(10,))
t2 = Thread(target=counter.increment, args=(20,))

t1.start()
t2.start()
t1.join()
t2.join()

print(f"The final counter value is : {counter.value}")