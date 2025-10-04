
num=[1,3,4,5,7]
for i in num:
    if i%2 ==0: 
        print("Even no found: ", i)
        break # after break statement control goes out of loop and else statement not execute.
else:
    print("All num are odd")

print("---"*10)
num=[1,3,7,5,7]
for i in num:
    if i%2 ==0:
        print("Even no found: ", i)
        break
else:  # else statement executes only after all the loop statement successfully execute.
    print("All num are odd")

print("--"*10)
#check if any name is missing
names=['ram','sita',None,'Hair']

for name in names:
    if name is None:
        print("Name is missing !!")
        break
else:
    print("All names are available")


print("--"*10)
#check if any name is missing
names=['ram','sita',"himal",'Hair']

for name in names:
    if name is None:
        print("Name is missing !!")
        break
else:
    print("All names are available")

print("*"*10)

#check the files are csv
files=['report.csv','data.pdf','list.csv']
for file in files:
    if not file.endswith(".csv"):
        print(f"{file} is not a csv file")
        break
else:
    print("All files are csv files !!!")


print("*"*10)

#check the files are csv
files=['report.csv','data.csv','list.csv']
for file in files:
    if not file.endswith(".csv"):
        print(f"{file} is not a csv file")
        break
else:
    print("All files are csv files !!!")


print("*"*10)
#check the duplicate files

files=['report.csv','data.csv','fils.csv','report.csv']

for file in files:
    if files.count(file)>1 :
        print(f"{file} Duplicate files exits here !")
        break

else:
    print("All files are unique !!!")


print("*"*10)
#check the duplicate files

files=['report.csv','data.csv','fils.csv','report.pdf']

for file in files:
    if files.count(file)>1 :
        print(f"{file} Duplicate files exits here !")
        break

else:
    print("All files are unique !!!")