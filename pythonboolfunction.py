name=""
email="ram@gmail.com"
phone="1235-1256"

#allow registration if any field is provided
print(any([name,email,phone]))

name="ram"
email="ram@gmail.com"
phone="1235-1256"
#allow registration only if all field is provided

print(all([name,email,phone]))

print("--"*10)

print(isinstance(123,int))
print(isinstance(12.3, float))
print(isinstance("abc",str))
print(isinstance(True,bool))

print("="*10)

print("Hello".endswith("o"))
print("Hello".startswith("H"))
print("Hello".startswith("h"))

OUTPUT
------------------------------
True
True
--------------------
True
True
True
True
==========
True
True
False
