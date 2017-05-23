class Point(object):
    ''' represents (x,y) in R2.'''
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distanceToOrigin(self):
        ''' returns distance to origin '''
        return (self.x**2 + self.y**2)**0.5

    def distance(self, other):
        ''' returns distance between points '''
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5


class Rectangle(object):
    def __init__(self,x,dx,y,dy):
        self.p1 = Point(x,y)
        self.p2 = Point(x+dx,y+dy)


        
a = Point(3,4)
b = Point(3,-4)

da =a.distanceToOrigin()
print(da)

g =a.distance(b)
print(g)

