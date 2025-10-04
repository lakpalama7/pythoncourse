
i=1
while i<4:
    print(i)
    i+=1

print("--"*10)

answer=""
''''
while answer.lower() != 'yes':
    answer = input("Do you agree (Yes/no): ")
print("Thank you")
'''
print("---"*10)

attempt=0
while attempt <3 : 
    user_input=input("Do you agree yes/no :")
    if user_input == 'yes':
        print("Glad you are in the same page !")
        break
    attempt+=1
else:   
    print("3 Strikes you are out !!!")   

# i=0
# while True:
#     i+=1
#     print(i)
#     if i>10:
#         break
# print("done")

OUTPUT:
------------------------
1
2
3
--------------------
------------------------------
Do you agree yes/no :no
Do you agree yes/no :no
Do you agree yes/no :may be
3 Strikes you are out !!!
