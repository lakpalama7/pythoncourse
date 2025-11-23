
text="This is a new content\nHello how are you"
f=open('demo.txt','w')
f.write(text)
print('Done writing')
f.close()

f=open('demo.txt','r')
print(f.read())
f.close()

print("Reading from the specifi location")
f=open('demo.txt','r')
f.seek(5) # text is read from the index 5 position
print(f.read())
f.close()

print("get the current position of the file pointer")
f=open('demo.txt','r')
f.readline()
print(f.tell())
f.close()