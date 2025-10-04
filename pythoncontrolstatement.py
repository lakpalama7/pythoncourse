
names = ["ram","hari","","rita"]

for name in names:
    if name == "":
        print("Name is empty is detected !")
        break
    print(f"Name: {name}")

print("---"*10)

names = ["ram","hari","","rita"]

for name in names:
    if name == "":
        continue
        print("continue execution")
    print(f"Name: {name}")

print("---"*10)

names = ["ram","hari","","rita"]

for name in names:
    if name == "":
        pass #todo - handle empty value latter.
    print(f"Name: {name}")

print("---"*10)
#team agreed to replace empty value with "unknown"
names = ["ram","hari","","rita"]


for name in names:
    if name == "":
        name = name.replace("","unknown")
    print(f"Name: {name}")
    

print("---"*10)
#skip weekends in the canlander loop

days=['mon','sun','tue','fri','sat']
weekends=['sun','sat']
for day in days:
    if day in weekends:
        continue
    print(f"Working day : {day}")

print("---"*10)

#scan list of emails and if any issue appears then exit from the loop.

emails=['ram@gmail.com','npl@gmail.com','fin@outlook.com','DROP TABLE USERS;','scam@hacker.com']

for email in emails:
    if ";" in email:
        print(f"SQL injection Hackar Attack Alert !!!")
        break
    print(f"Emails : {email}")

OUTPUT:
-------------------------
Name: ram
Name: hari
Name is empty is detected !
------------------------------
Name: ram
Name: hari
Name: rita
------------------------------
Name: ram
Name: hari
Name: 
Name: rita
------------------------------
Name: ram
Name: hari
Name: unknown
Name: rita
------------------------------
Working day : mon
Working day : tue
Working day : fri
------------------------------
Emails : ram@gmail.com
Emails : npl@gmail.com
Emails : fin@outlook.com
SQL injection Hackar Attack Alert !!!
