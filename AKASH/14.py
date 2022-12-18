n = int(input("Input an integer : "))
sum = 0
for i in range(3):
  h = int(pow(n, i+1))
  print(h)
  sum = sum + h
print("SUM IS :",sum)
