n=int(input("enter starting year"))
z=int(input("enter ending year"))
print ("the following are the leap years")

for i in range(n,z):
        if (i%400==0) and (i%100==0):
                print (i)


        elif (i%4==0) and  (i%100!=0):
                print(i)
