import math
class Point :
    def __init__(self,x,y,x1,y1) :
        self.x=x
        self.y=y
        self.x1=x1
        self.y1=y1
    def show(self) :
        print(self.x,self.y)
    def move(self) :
        print(self.y, self.x)
    def dist(self) :
        print(math.sqrt((self.x-self.x1)**2+(self.y-self.y1)**2))
x,y=map(int,input().split())
x1,y1=map(int,input().split())
a=Point(x,y,x1,y1)
a.show()
a.move()
a.dist()


