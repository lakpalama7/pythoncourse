import os

with open('D:\\github\\new.txt','r') as fp:
    print(fp.read())

print(os.listdir('D:\\github'))
print(os.path.isfile('D:\\github\\new.txt'))

new_filename="hello.txt"
path_name="D:\\github"

with open(os.path.join(path_name,new_filename),'w') as fp:
    fp.write("hello how are you, i am fine !!!")
    fp.close()
print("file write done")

file_path="D:\\github\\hello.txt"

if os.path.exists(file_path):
    print("File already exists")
    with open(file_path, 'a+') as fp:
        fp.write(" This is the last line\n")
        print("Append done")
        fp.seek(0)
        content=fp.read()
        print(content)
        fp.close()
