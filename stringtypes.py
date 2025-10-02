
#types --functions 1. types() 2. str() ---built in function
name = "ram"
print(type(name))

age=25
print(type(age))

#str() --- built in function
print("Your age is " + str(age))


#math --1. len() 2. count()

password="123456"
print(len(password))

text="""python is very popular
i love to learn python
python is easy to learn
python expert are very demanding
"""
print(text.count("python"))

#data transformation

price="1235,56"
price=price.replace(",",".")
print(price)

date_format="2025/10/26"
print(date_format.replace("/","-"))

newprice="$1,234.34"
print(newprice.replace("$","").replace(",",""))


newphoneno="+49 (176) 123-4567"
print(newphoneno.replace("+","").replace(" ","").replace("(","").replace(")","").replace("-",""))

first_name="davi"
last_name="hillary"
last_name=first_name + " " + last_name
print(last_name)

folder_path="C:/Users/ram/"
file_path="report.csv"
full_path = folder_path + file_path
print(full_path)

#f-string -- formated string
name="ram"
age=30
is_student = False
print("My name is "+name+" I am "+str(age)+"years old, my student status is"+str(is_student)+".")

#f-string 
print(f"My name is {name}. I am {age} years old. My student status is {is_student} .")

print(f"2+3 is {2+3}")

print(f"{{This is me}}")


#split()
stamp1="2025-10-25 10:25"
print(stamp1.split(" "))

stamp2 = "adam,23,finland,M,1989,012"
print(stamp2.split(","))

print("ha " * 3)
print("-" * 50)
print("*"*50)


#data---extraction
text="Python"
print(text[0])
print(text[-1])
print(text[-6])
print(text[0:5:2])

#white space cleaning
text=" hello world   "
print(text.lstrip())
print(text.rstrip())
print(text.strip())

text="###abc###"
print(text.strip("#"))
print(text.lstrip("#"))
print(text.rstrip("#"))

#case conversions
text="python PROGRAMMING"
print(text.lower())
print(text.upper())

data= "Email".lower()
search = "email".lower()
print(data==search)

data="968-Maria, ( Data Engineer ) ;; 27y "
name=data[4:9]
role=data[13:26].lower()
age=data[-4:-2]
print(f"name: {name} | role: {role} | age: {age}")


#search
print("search "*5)

phone = "+49-256-1253"
print(phone.startswith("+49"))

email="ram@gamil.com"
print(email.endswith("com"))
print(email.find("@"))
print("." in email)

if("@" in email):
    index=email.find("@")
    print("name :", email[ :index])


phone1="+42-125-2356"
phone2="00123-145-2365"
phone3="1452-145-8969"

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])


#validation
print("validation "*5)

country="USA"
print(country.isalpha())

country="USA1235"
print(country.isalpha())

phone="13562"
print(phone.isnumeric())

phone="135.62"
print(phone.isnumeric())