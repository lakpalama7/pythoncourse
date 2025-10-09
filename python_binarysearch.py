
pos=-1

def search(list,num):
    l=0
    u=len(list)-1

    while l <= u:
        mid=(l+u) // 2
        if list[mid]==num:
             globals()['pos'] = mid
             return True

        else:
            if list[mid] < num:
                l=mid+1
            else:
                u=mid-1
   
    return False

newlist=[56,67,43,21,34,11,23]
nlist=sorted(newlist)
print(nlist)
num=67
if(search(nlist,num)):
    print("value found at : ",pos)
else:
    print("value not found")