n=int(input("enter a number"))
k=1
if(n<0):
    print("negative numbers doesnt have factorial")
elif(n==0):
    print("factorial is 1")
else:
    for i in range(1,n+1):
     k=i*k
print(k)

