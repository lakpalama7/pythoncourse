import time
import csv



def task_file_decorator(fulltime=False):
    def task_decorator(func):
        def wrapper(*args,**kwargs):
            before=time.time()
            func(*args,**kwargs)
            after=time.time()
            total_time=after-before
            if fulltime:
                print(f"Total time taken for taks is :  {total_time} seconds")
                print(f"Function name is: {func.__name__}")
            else:
                print(f"Total time taken normally is : {total_time:.2f} seconds")
                print(f"Function name is : {func.__name__}")
        return wrapper
    return task_decorator


# @task_decorator
# def task_fun():
#     time.sleep(5)
#     print("Task function")

# task_fun()

@task_file_decorator(fulltime=True)
def task_file():
    time.sleep(3)
    with open("day_3/registration/student.csv","r") as file:
        file_reader=csv.reader(file)
        data=list(file_reader)
        

task_file()