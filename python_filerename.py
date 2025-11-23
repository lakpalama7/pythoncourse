import os

print("Rename the filename")
old_name='D:\\github\\test.txt'
new_name='D:\\github\\new1.txt'
os.rename(old_name,new_name)
print("rename done")

f=open('D:\\github\\new1.txt','r')
print(f.read())
f.close()
print("rading file done")

