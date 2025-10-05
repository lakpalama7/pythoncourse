
empty_list1=[] #manual creating or inserting data
empty_list2=list() #list function -- if data already avaiable or need to convert to list -- use list() function
print(empty_list1)
print(empty_list2)

list1=['a','b','c']
print(list1)
print(type(list1))

list2=[1,2,'a',2.3,None]
print(list2)
print(type(list2))

empty=list() #built in list() function to create a list
print(empty)
print("-"*10)

values=list("python")
print(values)

num_list=list(range(1,6))
print(num_list)

print("----"*10)
#nested list - matrix

matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','i']]
print(matrix)
print(type(matrix))

matrix1=list(range(5)),list(range(5,10)),list(range(10,15))
print(matrix1)

mixed_matrix=[[['a','b'],[1,2]],[["hello","world"],[True,False]]]
print(mixed_matrix)

OUTPUT:
-------------------------------
[]
[]
['a', 'b', 'c']
<class 'list'>
[1, 2, 'a', 2.3, None]
<class 'list'>
[]
----------
['p', 'y', 't', 'h', 'o', 'n']
[1, 2, 3, 4, 5]
----------------------------------------
[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
<class 'list'>
([0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14])
[[['a', 'b'], [1, 2]], [['hello', 'world'], [True, False]]]

