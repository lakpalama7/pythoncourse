#yield returns value --- generator obj is return and it is iterable 
def topTen():
    num=1
    while(num <=10):
        val=num*num
        yield val #returns value continuously each time next iterate
        num +=1


values=topTen()
print(values)
 
for i in values:
    print(i)