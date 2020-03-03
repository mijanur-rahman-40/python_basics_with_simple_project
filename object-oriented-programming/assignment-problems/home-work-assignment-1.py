"""
 problem : Fill in the Line class methods to accept coordinates
 as a pair of tuples and return the slope and distance of the line
"""


# solution 1
class Line:
    def __init__(self, color1, color2):
        self.color1 = color1
        self.color2 = color2

    def distance(self):
        x1, y1 = self.color1
        x2, y2 = self.color2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.color1
        x2, y2 = self.color2
        return (y2 - y1) / (x2 - x1)


c1 = (3, 2)
c2 = (8, 10)

myLine = Line(c1, c2)
print(myLine.distance())
print(myLine.slope())


# solution 2
class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * self.radius ** 2

    def surfaceArea(self):
        top = 3.14 * self.radius ** 2
        return 2 ** top + 2 * 3.14 * self.radius * self.height


myCylinder = Cylinder(2, 3)
print(myCylinder.volume())
