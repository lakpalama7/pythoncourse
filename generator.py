

def get_value():
    even=2
    while True:
        yield even #control execution is paused here ..till we ask next number.
        even+=2
    
obj=get_value()

for _ in range(10):
    print(next(obj))


#password checker

def guess_password():
    with open("test.txt","r") as file:
        file_reader=file.readlines()

        for line in file_reader:
            yield line.strip()



obj=guess_password()

while True:
    custom_pass="hello4536"
    try:
        pass_get=next(obj)
        if pass_get==custom_pass:
            print("Password is correctly guessed and password is: ", pass_get)
            break
    except Exception as e:
        print("Password searched is completed:")
        break



l1=[1,2,3,4,5,6,7,8]
l2=[num*2 for num in l1]
print(l2)

l3=[num for num in l1 if num%2==0]
print(l3)
l4=[num for num in l1 if num%2==1]
print(l4)

data=list(filter(lambda x: x*2, l1))
print(data)

data=list(filter(lambda x:x%2==0,l1))
print(data)

data=list(map(lambda x:x*x,l1))
print(data)