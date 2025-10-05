
lst=['a','b','c','d']
print(lst)
print(lst[0])
print(lst[-1])
print(lst[-2])
print(lst[2])

print("--"*10)

matrix1=[['a','b','c'],
         [1,2,3],
         ['d','e','f']]
print(matrix1)
print(matrix1[2])
print(matrix1[-1])
print(matrix1[2][2])
print(matrix1[-1][-1])
print(matrix1[0][-1])

print("--"*10)

#slicing list
data=['a','b','c','d']
print(data)
print(data[:2]) #a,b
print(data[1:3]) #b,c
print(data[2:]) #c,d
print(data[:]) #a,b,c,d
print(data[-2:])

print("--"*10)

matrix1=[['a','b','c'],
         [1,2,3],
         ['d','e','f']]

print(matrix1[:2])
print(matrix1[0:2])
print(matrix1[1:])
print(matrix1[-2:])
print(matrix1[:])
print("---"*10)

print(matrix1[-1][:2])
print(matrix1[1][1:])
print(matrix1[1][-1])
print(matrix1[2][1:])

OUTPUT:
------------------
['a', 'b', 'c', 'd']
a
d
c
c
--------------------
[['a', 'b', 'c'], [1, 2, 3], ['d', 'e', 'f']]
['d', 'e', 'f']
['d', 'e', 'f']
f
f
c
--------------------
['a', 'b', 'c', 'd']
['a', 'b']
['b', 'c']
['c', 'd']
['a', 'b', 'c', 'd']
['c', 'd']
--------------------
[['a', 'b', 'c'], [1, 2, 3]]
[['a', 'b', 'c'], [1, 2, 3]]
[[1, 2, 3], ['d', 'e', 'f']]
[[1, 2, 3], ['d', 'e', 'f']]
[['a', 'b', 'c'], [1, 2, 3], ['d', 'e', 'f']]
------------------------------
['d', 'e']
[2, 3]
3
['e', 'f']
