n=int(input("enter the no . of elements"))
print("enter the elements")
list=[]
for i in range(0,n):
    i=input()
    list.append(i)
print(list)
count=0
for i in list:
    for j in i:
        if j=='a':
            count=count+1
print(count)
