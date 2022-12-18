n=input("enter a text")
dict={}
a=n.split()
print(a)
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1


for m,k in dict.items():
    print(m,k)
