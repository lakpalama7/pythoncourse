
class AgeError(Exception):
    pass

def set(age):
    if age < 0:
        raise AgeError("Age  be less than zero")
    print(f"Age is : ", age)

try:
    set(2)

except AgeError as e:
    print("Error : ", e)


