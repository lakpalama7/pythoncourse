
a=5
b=1

try:
    print("resource open")
    print(a/b)
    
except ZeroDivisionError as e:
    print("Hey cannot divide by zero: ",e)

except Exception as e:
    print("something is wrong...!!!")

finally:
    print("resource closed")
    print("first try block execute finally")

print("first try block")



try:
    num=(int(input("Enter the value : ")))
    print(num)
except ValueError as e:
    print("invalid number :",e)
except Exception as e:
    print("something is wrong...!!!")
finally:
    print("second block execute finally")

print("second try block end")