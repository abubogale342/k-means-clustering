class Cluster(object):
        def init(self, x, y):
            self.center = Point(x, y)
            self.points = []

        def update(self):
            for i in range(len(self.points)):
                self.center.x += self.points[i][0]
                self.center.y += self.points[i][1]
            self.center.x = self.center.x/len(self.points)
            self.center.y = self.center.y/len(self.points)

        def add_point(self, point):
            self.points.append(point)
======================================
import matplotlib.pyplot as plt 
