
#baseexception is root of all exception. they are not consider "normal errors" like systemexit, keyboard interrup error
try:
    raise BaseException("This is a base exception")
except BaseException as e:
    print(e)

#exception base class for all catchable errors like valueerror, typeerror, filenotfound, dividebyzero
try:
    raise Exception("this is generic exception")
except Exception as e:
    print(e)

#Arithmetic error base for all mathematic error

try:
    raise ArithmeticError("Arithmetic error")
except ArithmeticError as e:
    print(e)

#division by zero - 
try:
    result=10/0
except ZeroDivisionError as e:
    print(e)

try:
    print(var)
except NameError as e:
    print(e)