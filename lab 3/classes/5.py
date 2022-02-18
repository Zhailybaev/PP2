class Account :
    def __init__(self,owner,balance) :
        self.owner=owner
        self.balance=balance
    def deposit(self, dep) :
        self.balance=self.balance+dep
    def withdraw(self,wt) :
        if self.balance>=wt :
            self.balance=self.balance-wt
            print("We can do it")
        else :
            print("we can not do it")
    def print(self) :
        print(self.balance)

a,b=map(int,input().split())
dep=int(input())
wt=int(input())
n=Account(a,b)
n.deposit(dep)
n.withdraw(wt)
n.print()
