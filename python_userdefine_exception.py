class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age=age
        self.msg=msg
        super().__init__(self.msg)

    def __str__(self):
        return (f'{self.age} -> {self.msg}')
    
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to : {age}")


try:
    
    set_age(150)
   
except InvalidAgeError as e:
    print(e)
    print("type: ", type(e))
    print("Msg : ", e.msg)
    print("age: ", e.age)
    print(e.__dict__)
    print(e.__str__())


class NetworkError(RuntimeError):
    def __init__(self, args):
        self.args=(args,)

try:
    raise NetworkError("Connection failed !!!")

except NetworkError as e:
    print(e.args)