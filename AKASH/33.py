class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    def perimeter(self):
         return 2*(self.length+self.breadth)

a=int(input("enter the length"))
b=int(input("enter the breadth"))
o=rectangle(a,b)
y=o.area()
x=o.perimeter()
print("the area is",y)
print("the perimeter is:",x)

c=int(input("enter the length"))
d=int(input("enter the breadth"))

p=rectangle(c,d)
e=p.area()
f=p.perimeter()
print("the area is",e)
print("the perimeter is:",f)

if (y>e):
    print("the first rectangle is greater than second")
elif(y==e):
    print("the areas are equal")
else:
    print("the second rectangle is greater than first")

