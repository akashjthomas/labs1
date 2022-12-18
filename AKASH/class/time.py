class Time:
    def __init__(self,hour,minute,seconds):
        self.hour=hour
        self.minute=minute
        self.seconds=seconds
    def __add__(self, other):
        return self.hour+other.hour,self.minute+other.minute,self.seconds+other.seconds
o1=Time(6,11,5)
o2=Time(4,7,1)
print("sum of 2 time:",o1+o2)
