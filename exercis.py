from math import sqrt

class Point(object):

    def init(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        D = sqrt(((self.x.sub(other.x))**2).add((self.y.sub(other.y))**2))
        return D
    
    def repr(self):
        return "Point(%d, %d)" % (self.x, self.y)

    def add(self, other):
        total_x = self.x + other.x
        total_y = self.y + other.y
        return Point(total_x, total_y)
    
    def sub(self, other):
        total_sub_x = self.x - other.x
        total_sub_y = self.y - other.y
        return Point(total_sub_x, total_sub_y)
    
    def mul(self, other):
        return self.x * other.x + self.y * other.y