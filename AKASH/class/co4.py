class Rectangle:
    def __init__(self,__length,__breadth):
        self.__length=__length
        self.__breadth=__breadth

    def area(self):
        return self.__length*self.__breadth

a=int(input("enter the length"))
b=int(input("enter the breadth"))
o=Rectangle(a,b)
y=o.area()
print("the area is",y)

c=int(input("enter the length"))
d=int(input("enter the breadth"))

p=Rectangle(c,d)
e=p.area()
print("the area is",e)

if (y>e):
    print("the first rectangle is greater than second")
elif(y==e):
    print("the areas are equal")
else:
    print("the second rectangle is greater than first")





