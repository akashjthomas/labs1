n=int(input("enter the no . of elements"))
print("enter the elements")
list=[]
for i in range(0,n):
    i=int(input())
    if(i>100):
        list.append("over")
    else:
        list.append(i)
print(list)
