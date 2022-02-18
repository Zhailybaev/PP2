class Rectangle :
    def __init__(self,length, width) :
        self.length=length
        self.width=width
    def comp(self) :
        area=self.length*self.width
        print(area)

a=int(input())
b=int(input())
x=Rectangle(a,b)
x.comp()