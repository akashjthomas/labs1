class rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
        self.area = length * breadth
        print("\nLength = ", self.__length, "\nBreadth = ", self.__breadth)

    def __lt__(self, other):
        if self.area < other.area:
            return "Rectangle 1 is smaller than rectangle 2"
        else:
            return "Rectangle 1 bigger than rectangle 2"

r1 = rectangle(20, 30)
r2 = rectangle(10, 20)
print(r1 > r2)

