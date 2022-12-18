a=int(input("enter upper limit:"))
b=int(input("enter lower limit:"))
lists=[]

    # Traverse through all numbers
if a>999 and a<10000  and b<10000 and b>999:


    for i in range (a,b+1):
        for j in range(1,i):
            if j * j == i:
                string = str(i)
                if int(string[0]) % 2 == 0 and int(string[1]) % 2 == 0 and int(string[2]) % 2 == 0 and int(
                        string[3]) % 2 == 0:
                    lists.append(string)
else:
  print("invalid input")
print(lists)
