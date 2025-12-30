
player_list=[]

def show_players_info(player_list):
    for item in enumerate(player_list,start=1):
       print(item)


# while True:
#     player_name=input("Enter player name or 'q' to quit:").lower()

#     if player_name == 'q':
#         break

#     player_list.append(player_name)

# show_players_info(player_list)

a, *_, b=["a","b","c","d"]
print(a, b)
x,*all,y=(1,2,3,4,5)
print(x,all, y)


data={"a","b","a","c","d",1,2,3,3}
print(data)
data.add("hi")
data.add(100)
print(data)
data.remove("hi")
print(data)

print(list())
print(tuple())
l=[1,2,1,'a','b','a']
l=(1,2,1,'a','a','b')
s=set()
s.add('z')
s.add('a')
print(s)
print(dict())


data={'name':'sonam','age':24,'city':'bangalore'}
print(data)
print(data.keys())
print(data.values())
print(data.items())
data['age']=50
data['phone']=1234567890
print(data)

name=data.get('name')
print(name)
for k,v in data.items():
    print(k,v )

print("age" in data.keys())
print(50 in data.values())
print(('age',50) in data.items())

for data in 'apple':
    print(data)


for k, v in enumerate("apple"): #[(0,'a'),(1,'p'),(2,'p'),(3,'l'),(4,'e')]
    print(k, v)


a="appleaaaaabbbbbaaaaabbbbbaaaa  abbbbb bbbbbbbbbb  bbbbbbbbbbbbbbbbb ggggggggggggggg  gggggggggggggggggggg"
b="appleaaaaabbbbbaaaaabbbbbaaaa  abbbbb bbbbbbbbbb  bbbbbbbbbbbbbbbbb ggggggggggggggg  gggggggggggggggggggg"
a="hello"
b=a
b="world"
print(a is b)


print("***"*10)

import time
value={}

def heavy_task(num):

    if num in value.keys():
        print("data already present in cache")
        return value[num]
    print("calculating...")
    time.sleep(5)  #simulating heavy task by adding delay
    res=num**2
    value[num]=res
    return res

print("first time call",heavy_task(5))
print("second time call",heavy_task(5))
print("third time call",heavy_task(5))

print(value)