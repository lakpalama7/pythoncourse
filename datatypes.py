#data types in python --
#python automatically detects datatypes
#dynamic - can be changed at any time.
"""Three categories of datatypes
1. No Value - Nonetype
2. Single value - int, float, complex, string, bool, date and time
3. Multi value - list, set, tuple, dict"""
'''Values are the object of data types class, each data types class has methods and value can access all the method of its data type class
but it is restricted to access the methods of other data type class but some cases can access the method
e.g 'Hello' string class object and 'Hello' can access all the method of string class but restricted from other class method like int, float etc.
'''

a = 10 #int
b = 2.21 #float
c = "hello" #str
d = 'hi' #str
e = True #bool
f = False #bool
g = None #noonType --- python cannot determine its type so variable is not created
h = "" #string -- with no value --- variable is crreated since it is string type
i = " " #string -- with value space between " " --variable is created since it is string and has space between.

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)


num = 10
text = 'hi'
print(type(num))
print(type(text))
print(len(text))
print(text.upper)
print(pow(num,2))
print(num.bit_length())

-------------------------------------------------------
output:
10
2.21
hello
hi
True
False
None


<class 'int'>
<class 'str'>
2
<built-in method upper of str object at 0x00007FFF30C7B3B8>
100
4
