try:
    with open('hello.txt','w') as f:
        f.write("My First Hello World")

except FileExistsError as e:
    print(e)

finally:
    print("Done")

try:
    with open('hello.txt','rb') as f:
        print(f.read(8).decode('utf-8')) #read My First
        print("Current position of pointer :", f.tell())
        f.seek(-5,1)
        print(f.read(11).decode('utf-8'))
        f.seek(-5,1)
        print("Current position of pointer: ", f.tell())
        print(f.read(11).decode('utf-8'))
        f.seek(-20,1)
        print("current position of pointer: ", f.tell())
        print(f.read(20).decode('utf-8'))
except FileExistsError as e:
    print(e)