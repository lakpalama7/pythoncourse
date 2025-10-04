
#membership operator - in , not in

print("o" in "python")
print("i" in "python")
print("i" not in "python")
print("-"*10)

print(1 in [1,2,3])
print(2 not in [1,3,4,5])
print(2 in [1,3,4,5])
print("---"*10)
#secutiry check that domain is not banned

domain="gmail.com"
banned_domain=["span.com","fake.org","bot.net"]
print(domain not in banned_domain)
print("--"*10)
#identity operator - is , is not

#for multiple value python create a differnt id for each object.
a = [1,2,3]
b = [1,2,3]
print(a == b) # value is check - value are equal
print(a is b) # object id/memory address is check but it is different

a = [1,2,3]
b = a  # b not points to same id of object a
print(a == b) # value is check - value are equal
print(a is b) 

print("-"*10)

#for single value python share the same object id with the variables.
a = "hello"
b = "hello"
print(a == b)
print(a is b)

a = "hello"
b = a
print(a == b)
print(a is b)

print("--"*10)
#make sure the email exits and it is not blank

email="" #it is empty but it is str type
print(email!="")
email="ram@gmail.com"
print(email!="")
email=None  #no value at all and its type is unknown
print( email is not None and email!="")