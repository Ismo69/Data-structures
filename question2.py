import math 
class Point:

    '''Creates a point on a coordinate plane with values x and y.'''
    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.x = x
        self.y = y

    def move(self, dx, dy):
        '''Determines where x and y move'''
        self.x = self.x + dx
        self.y = self.x + dy

    def __str__(self):
        return "Point(%s,%s)"%(self.x, self.y) 


    def getX(self):
        return self.x

    def getY(self):
        return self.y




class Rectangle:
    def __init__(self, bottomLeftCorner = Point(0,0), topRightCorner = Point(1,1)):
        self.bottomLeftCorner = bottomLeftCorner
        self.topRightCorner = topRightCorner
        self.height = topRightCorner.y - bottomLeftCorner.y
        self.width = topRightCorner.x - bottomLeftCorner.x

    def rec_perimeter(self):
        self.perimeter = (self.height + self.width) * 2
        return self.perimeter

    def rec_area(self):
        self.area = self.height * self.width
        return self.area
    
    def intersect(RecA, RecB, Rec1, Rec2): 

rec = Rectangle(Point(0,0),Point(12,12))
print(rec.area)  
print(rec.perimeter) 

recA = rectangle(Point(2, 4), Point(8, 8))
recB = rectangle(Point(4, 8), Point(10, 10))


rec.intersect(recA.bottomLeftCorner, recA.topRightCorner, recB.bottomLeftCorner, recB.topRightCorner)
