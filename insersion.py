items=[3,5,75,2,8,0,0]
i=0
while(i<len(items)):
    j=i+1
    while j<len(items):
        if items[j]<items[i]:
            temp=items[j]
            items[j]=items[i]
            items[i]=temp
        j=j+1
    i=i+1
print(items)
