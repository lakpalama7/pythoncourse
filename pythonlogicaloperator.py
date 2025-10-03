

print(3>2 and 5==5)
print(3>1 and 5!=5)

print(2>1 or 5==5)
print(2>5 or 3>1)
print(1>2 or 1>3)

print("---"*10)
#check if the system is under pressure 
cpu_uses=70
memory_uses=95
print(cpu_uses > 90 or memory_uses > 90)

#after cool down
cpu_uses=70
memory_uses=80
print(cpu_uses > 90 or memory_uses > 90)

print("---"*10)
#checking user credential 
username=True
password=False
print(username and password)

username=True
password=True
print(username and password)

print("--"*10)
print(not 3>2)
print(not 5 ==9 )
print(not True)
print(not False)
print("---"*10)

print(not not False)


#allow acces if user is login or guest user
#but they must not be banned
is_login=True
is_guest=False
is_banned=False
print((is_login or is_guest) and not is_banned)

is_login=False
is_guest=True
is_banned=True
print((is_login or is_guest) and not is_banned)

print("=="*10)

user="Ram"
print(user is not None)
print(isinstance(user,str))
print(len(user)!=0)


OUTPUT
________________________
True
False
True
True
False
------------------------------
True
False
------------------------------
False
True
--------------------
False
True
False
True
------------------------------
False
True
False
====================
True
True
True
