score=90
project=True
if score >=90:
    if project:
        print("A+")
    else:
        print("A") 
elif score >=80:
      if project:
        print("B+")
      else:
        print("B") 
elif score >=70:
    if project:
        print("C+")
    else:
        print("C") 
elif score >=60:
     if project:
        print("D+")
     else:
        print("D") 
elif score >=50:
     if project:
        print("E+")
     else:
        print("E") 
else:
    print("F")


#email validation

email="ram@gmail.com"
email=email.strip()
check=True

if email is None and email =="":
    print("Email cannot be empty")
    check=False
#check @ and . in email

if not("."in email and "@"  in email):
    print("email does not contain @ and . ")
    check=False

#check only one @ exit in email

if email.count("@") != 1:
    print("Email must contain only one @")
    check=False

#email must end with .org or .com or .net

if not(email.endswith((".com",".org",".net"))):
    print("Email must end with one of the .org or .com or .net")
    check=False

#email must not be grater than 50 characters
if len(email) > 50:
    print("Email lenght must not be greater than 50 characters")
    check=False

#email must start with text or digits only
if not(email[0].isalnum() and  email[-1].isalnum()):
    print("Email must start/end with text or digit only")
    check=False

if check:
    print("Email is valid")

OUTPUT:
--------------
A+
Email is valid

   



