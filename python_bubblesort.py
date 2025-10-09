
def bubblesort(values):
   
    for i in range(len(values)-1,0,-1):
        for j in range(i):
            if(values[j]>values[j+1]):
                temp=values[j]
                values[j]=values[j+1]
                values[j+1]=temp
      


data=[2,4,5,1,3,9,99,100,23,2,1,0]
bubblesort(data)
print(data)