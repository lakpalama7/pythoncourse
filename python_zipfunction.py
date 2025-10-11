
name=['nabin','ram','shyam','sita','nabin']
company=['dell','hp','apple','acer','dell']

zipped=zip(name,company)
for (a,b) in zipped:
    print(a,b)

print("---"*10)

zipped=list(zip(name,company))
print(zipped)

print("---"*10)
zipped=set(zip(name,company)) #unique values and unorder list
print(zipped)

print("----"*10)
zipped=tuple(zip(name,company))
print(zipped)

print("---"*10)
zipped=dict(zip(name,company))
print(zipped)