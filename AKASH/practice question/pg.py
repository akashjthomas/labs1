list1=['aron','ashwathy']
print(list1)
list2=[]
for item in list1:
    for ele in item:
        res=ord(ele)
        list2.append(res)
print(list2)

