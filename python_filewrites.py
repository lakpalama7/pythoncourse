
content=['name: hari','\nAddress:india','\nage:30','\ndegree: masters']

try:
    with open('hello.txt','w+') as f:
        f.write("Student Details: \n")
        f.writelines(content)
        f.seek(0)
        print(f.read())
except FileNotFoundError as e:
    print(e)
finally:
    print("Write and read done |||")


content1=['name:sita','\nGender:Female','\nAge:30','\nDegree:phd']
try:
    with open('hello.txt','a+') as f:
        f.write("\n Female Student:\n")
        f.writelines(content1)
        f.seek(0)
        print(f.read())
except FileExistsError as e:
    print(e)

finally:
    print("Append and read done |||")

try:
    with open('hello.txt','r+') as f:
        f.seek(0,2) #place the pointer at the end of file
        f.write("\n This is the end of the file")
        f.seek(0)
        print(f.read())

except FileExistsError as e:
    print(e)

finally:
    print("File write and read done!!!")
