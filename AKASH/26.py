n=input("enter a string")
dict={}
for i in n:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for m,k in dict.items():
    print(m,k)



print(dict)
