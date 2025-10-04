

for i in (1,2,3,4,5):
    print("Round: ",i)

print("-"*10)
for i in (1,2,3,4,5):
    print(f"Round :{i}")

print("--"*10)

items=('a','b','c','d') #tuple
for item in items:
    print(f"Item : {item}")

print("-"*10)

items=[1,2,3,4,5] #list
for item in items:
    print(f"Rounded : {item}")

print("--"*10)
country="united state" #string
for i in country:
    print(f"items :{i}")

print("--"*10)
#using loop in range()

for i in range(5): #start from 0 to 4
    print(f"range: {i}")

print("--"*10)

for i in range(1,5): #value start from 1 and stop at 5
    print(f"item : {i}") #output: 1,2,3,4 

print("---"*10)

for i in range(1,10,2): #display value between 1 to 10 based on the increament  2 
    print(f"item : {i}")

print("--"*10)

#use loop - to move through the data and perform aggregrate function like sum, avg, count.
scores=[1,2,3,4,5]
total=0
for score in scores:
    total +=score
    print("Current total is :", total)
print(f"total score : {total}")

print("---"*10)
#use loop - for data transformation like cleaning before data processing

files=["  Report.csv","DATA.csv","finaL.TXT  "," file.excel"]

for file in files:
    
    file = file.strip().lower().replace(".txt",".csv").replace(".excel",".csv")
    print(f"After Cleaning : {file}")



print("---"*10)
num=7
for i in range(1,11):
    print(f"{num}*{i} = {num *i}")

print("--"*10)

for i in range(7):
     print("*" * i)
