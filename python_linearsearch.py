
pos=-1
def search(list,n):
    i=0
    while i<len(list):
        if(list[i]==n):
            globals()['pos']=i
            return True
        i+=1
    return False
        


list=[4,7,8,9,2,3,0]
n=3
if(search(list,n)):
    print(f"the value: {n} Found at position: {pos}")
else:
    print(f"the value: {n} not found")