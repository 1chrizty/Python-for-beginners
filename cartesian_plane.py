''' Plot points on a cartesian plane which has 2 coordinates x and y 
    1. define class point, its instance should have 2 attributes x and y, define x and y, default value must be zero
    2. define an instance method reset()
        who called it will set x,y values to zero(ie it will set the points to original(0,0))
    3. define an methd move()
        this should change values of x, y
    4. use this move method to update reset() method
    5. define 2 methods xmove and ymove
        this should move the values of x and y seperately'''


class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def reset(self):
        # self.move(0,0)
        self.x = 0
        self.y = 0
    def move(self,a,b):
        self.x = a
        self.y = b
        return a,b
    def xmove(self,a):
        self.x = a
    def ymove(self,b):
        self.y = b
num = Point(2,5)
print(num.x,num.y)
num.reset()
print(num.x,num.y)
num.move(3,4)
print(num.x,num.y)
num.xmove(5)
print(num.x,num.y)
num.ymove(8)
print(num.x,num.y)