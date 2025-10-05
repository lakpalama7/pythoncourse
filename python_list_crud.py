
data=['a','b',1,2,'c']
data.append('x')
print(data)
data.append(10)
print(data)

data.insert(2,'d')
print(data)

print("--"*10)
matrixs=[['a','b','c'],
         [1,2,3],
         ['d','e','f']]
print(matrixs)
matrixs.append([4,5,6])
print(matrixs)
matrixs.insert(2,[10,11,12])
print(matrixs)
matrixs.pop()
print(matrixs)
matrixs.remove([1,2,3])
print(matrixs)

print("--"*10)
matrixs=[['a','b','c'],
         [1,2,3],
         ['d','e','f']]

matrixs[1].append("x")
print(matrixs)
matrixs.append([10,11,12])
print(matrixs)
print(matrixs[1][-1])
print(matrixs[1][2:])

matrixs[1].insert(3,"z")
print(matrixs)

remove1=matrixs.pop(0)
print(matrixs)
print("Remove item is : ", remove1)
popitem=matrixs.pop()
print(matrixs)
print("pop item is : ", popitem)
remove_oneitem=matrixs[0].pop()
print(matrixs)
matrixs[0].pop()
print(matrixs)
matrixs.clear()
print(matrixs)

print("---"*10)
num=[1,2,3,4,5]
num[-1]=10
print(num)

num[0]=0
print(num)

num[:2]='a','b'
print(num)

num[-2:]='x','y'
print(num)


print("--"*10)
matrixs=[['a','b','c'],
         [1,2,3],
         ['d','e','f']]
matrixs[-1]=[10,20,30]
print(matrixs)

matrixs[0][ : :2]='x','y'
print(matrixs)

matrixs[-1][::2]=100,300
print(matrixs)

matrixs[1][:2]=11,22
print(matrixs)

matrixs[1][-2:]=222,333
print(matrixs)

OUTPUT:
----------------------------
['a', 'b', 1, 2, 'c', 'x']
['a', 'b', 1, 2, 'c', 'x', 10]
['a', 'b', 'd', 1, 2, 'c', 'x', 10]
--------------------
[['a', 'b', 'c'], [1, 2, 3], ['d', 'e', 'f']]
[['a', 'b', 'c'], [1, 2, 3], ['d', 'e', 'f'], [4, 5, 6]]
[['a', 'b', 'c'], [1, 2, 3], [10, 11, 12], ['d', 'e', 'f'], [4, 5, 6]]
[['a', 'b', 'c'], [1, 2, 3], [10, 11, 12], ['d', 'e', 'f']]
[['a', 'b', 'c'], [10, 11, 12], ['d', 'e', 'f']]
--------------------
[['a', 'b', 'c'], [1, 2, 3, 'x'], ['d', 'e', 'f']]
[['a', 'b', 'c'], [1, 2, 3, 'x'], ['d', 'e', 'f'], [10, 11, 12]]
x
[3, 'x']
[['a', 'b', 'c'], [1, 2, 3, 'z', 'x'], ['d', 'e', 'f'], [10, 11, 12]]
[[1, 2, 3, 'z', 'x'], ['d', 'e', 'f'], [10, 11, 12]]
Remove item is :  ['a', 'b', 'c']
[[1, 2, 3, 'z', 'x'], ['d', 'e', 'f']]
pop item is :  [10, 11, 12]
[[1, 2, 3, 'z'], ['d', 'e', 'f']]
[[1, 2, 3], ['d', 'e', 'f']]
[]
------------------------------
[1, 2, 3, 4, 10]
[0, 2, 3, 4, 10]
['a', 'b', 3, 4, 10]
['a', 'b', 3, 'x', 'y']
--------------------
[['a', 'b', 'c'], [1, 2, 3], [10, 20, 30]]
[['x', 'b', 'y'], [1, 2, 3], [10, 20, 30]]
[['x', 'b', 'y'], [1, 2, 3], [100, 20, 300]]
[['x', 'b', 'y'], [11, 22, 3], [100, 20, 300]]
[['x', 'b', 'y'], [11, 222, 333], [100, 20, 300]]
