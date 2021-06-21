list=[]
for x in range(1,11):
    val=input("Enter values:")
    list.append(val)  
    print(list)
    if int(val)>10:
        count=count+1
print(count)