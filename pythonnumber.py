import math
import random

a=10
b=2.34
c=2+2j
print(type(a))
print(type(b))
print(type(c))

num="20"
print(type(num))
print(num *3)

num=int(num)
print(type(num))
print(num*2)

a=2.3
print(int(a))
a=10
print(float(a))

x=10 #real
y=3  #imaginary
print(complex(x,y))

print("---" *10)
print(4+2)
print(5-2)
print(2*3)
print(9/2)
print(9//2) #gives the round down value
print(5%2) #gives the reminder value
print(2**3) #gives 2 power 3 product

print("---" *10)
x=2
x+=3
print(x)

y=5
y*=2
print(y)

print("--"*10)

#abs() -- return absolute value without negative 

print(2-10)
print(abs(2-10))

price=23.232343454545
print(round(price))
print(round(price,2))

price=23.5689554
print(round(price))
print(round(price, 2))

print("---" *10)
#math module
price = 23.4545
print(math.floor(price))
print(math.ceil(price))

print(math.trunc(price)) #trunc() removes all value after decimal 
print(int(price))

print("---"*10)

print(random.random()) #generate random number between 0 and 1.
print(random.randint(1,10)) #generate random number between (start, end) 

print("---"*10)

x=3.0
print(x.is_integer()) #its a whole number 0 after decimal is ignored

y=3.1
print(y.is_integer()) #it not a whole number 1 after decimal ....its float number

print("==="*10)
print(isinstance(y,int)) # 3.1 is float so false
print(isinstance(y,float)) # 3.1 is float so true