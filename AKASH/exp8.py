a=input("enter a string")
b=a[0]
for i in a:
    if i==b:
         a=a.replace(i,"$")

a=b+a[1:]
print(a)
