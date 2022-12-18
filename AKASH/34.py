class bank:
    def __init__(self,accn,name,accty):
        self.accn=accn
        self.name=name
        self.accty=accty
        self.bal=0

    def showamt(self):
        print("account holder name:",self.name)
        print("account Number:", self.accn)
        print("account type:", self.accty)
        print("your balance is:", self.bal)

    def dep(self,d1):
        self.bal=self.bal+d1
        return self.bal

    def wdraw(self,w1):
        self.bal=self.bal-w1
        return self.bal

a=input("enter your name")
b=int(input("enter your account number"))
c=input("enter account type")
d=0
e=bank(a,b,c)
print("\ndeposit")
e.showamt()
while(True):
    print("\nMENU")
    print("\n withdraw")
    q=int(input("enter your choice"))
    if (q==1):
        d=int(input("enter the amount to deposit:"))
        print("your total balance amount is:",e.dep(d))
    elif(q==2):
        w=int(input("enter the amount to be withdrawn:"))
        if(w>d):
            print("insufficient balance")
        else:
            print("your total balance amount is:",e.wdraw(w))
    else:
        print("enter a valid choice")
