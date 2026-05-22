
from threading import Event, Thread
from time import sleep

def task(event,id):

    print(f"Thread id: {id} is waiting for the event to be set.")
    event.wait()
    print(f"Thread id: {id} has received the event.")

event = Event()
t1 = Thread(target=task, args=(event, 1))
t2 = Thread(target=task, args=(event,2))

t1.start()
t2.start()

print("main thread is sleeping for 3 seconds before settign the event set")
sleep(3)
event.set()
