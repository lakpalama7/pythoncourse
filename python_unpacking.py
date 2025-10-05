
person=['maria',29,'data science','spain']

name,age,role,country = person
print(name)
print(age)
print(role)
print(country)

print("--"*10)

person=['maria',29,'data science','spain']

name, *details,country = person # *asteriks stores values as list of values.
print(name)
print(details)
print(country)
print("---"*10)
name, *rest_details=person
print(name)
print(rest_details)

print("---"*10)
test="Hello"
first,second,third,fourth,fifth=test
print(first)
print(third)

print("--"*10)
person=['maria',29,'data science','spain']

name, _ , role, _ = person # underscore - avoids values - frees memory
print(name)
print(role)

print("--"*10)
num=[1,2,3,4,5,6,7]
first, *details, last=num
print(first)
print(details) #it holds all the middle values
print(last)


print("--"*10)
num=[1,2,3,4,5,6,7]
first, *_ , last=num # *_ does not store value it avoids all value
print(first)
print(last)

# _ single underscore avoids one value only ....*_ avoids multiple value in sequence