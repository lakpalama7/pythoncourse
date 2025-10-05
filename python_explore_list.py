
num=[1,2,4,9,10,1,1]
print("Max :", max(num))
print("Min : ", min(num))
print("Sum : ", sum(num))
print("Len : ", len(num))

print("--"*10)
print("Count: ", num.count(1))
print("Index of 10: ", num.index(10))
print("Pop item: ", num.pop())
print(num)
print("--"*10)
num.sort()
print(num)
num.reverse()
print(num)
num.insert(0,20)
print(num)
num.remove(1)
print(num)
num.sort()
print(num)
print("---"*10)
print(20 in num)
num.insert(0,1)
print(num)
print(num.count(1))

print("--"*10)

print("All: ", all([1,2,3,4,5]))
print("All : ", all([1,2,0,3,0]))
print("Any : ", any([1,2,3,4]))
print("Any : ", any([1,0,0,2,3,None]))

print([1,-2,2,3,-4].index(-4))

print("---"*10)
num=[1,2,4,9,10]
print(4 in num)
print(3 in num)
print(8 not in num)

print("---"*10)

a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)

print("---"*10)
a=[1,2,3]
b=a
print(a==b)
print(a is b)

print("---"*10)
a=[3,3,5]
b=[3,3,4]
print(a>b)
