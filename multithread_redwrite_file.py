
from time import sleep, perf_counter
from threading import Thread



def replace(filename, oldtext, newtext):
    with open(filename,'r') as f:
        print(f"Reading file name: {filename} content: ")
        content=f.read()
        content=content.replace(oldtext,newtext)

    with open(filename,'w') as f:
        f.write(content)

def main():

    filelist=[
        "./dist/sales/test1.txt",
        "./dist/sales/test2.txt",
        "./dist/sales/test3.txt",
        "./dist/sales/test4.txt",
    ]



    thread = [Thread(target=replace,args=(filename, 'lakpa','sherpa')) for filename in filelist]

    for t in thread:
        t.start()


    for t in thread:
        t.join()


if __name__ == '__main__':       
    start = perf_counter()
    main()
    end = perf_counter()

print(f"The time take is : {end - start:.2f}")