
#writing one file data into another file
f=open("filedata.txt", 'r') #readcharacter

f1=open("testdata",'w') #write character

for data in f:
     f1.write(data)


#writing one image binarydata to another image
image1=open('image1.png','rb') #readbinary
image2=open('image2.png','wb') #writebinary

for data in image1:
    image2.write(data)


