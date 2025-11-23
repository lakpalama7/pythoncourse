import shutil
import os

src_path='D:\\text.txt'
dst_path='D:\\github\\test.txt'

shutil.copy(src_path,dst_path)
print("copied")

f=open(r'D:\github\test.txt','r')
print(f.read())
f.close()

