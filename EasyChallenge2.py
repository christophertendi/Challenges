import math

class Circle():
    def __init__(self,radius = 1.0,color = "red"):
        self.radius = radius
        self.color = color

    def getRadius(self):
        return self.radius

    def setRadius(self,radius):
        self.radius = radius

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color = color

    def __str__(self):
        return ('circle radius:' + str(self.getRadius()) + " colour of circle: " + self.getColor())
    
    def getArea(self):
        return (math.pi * self.getRadius()**2)

class Cylinder(Circle):

    def __init__(self,height = 1.0, radius = 1.0, color = "red" ):
        self.height = height
        super().__init__(radius, color)
        
    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def __str__(self):
        return ('cylinder radius: ' + str(self.getRadius()) + " cylinder colour: " + self.getColor() + " height: " + str(self.getHeight()))

    def getVolume(self):
        return (self.getArea() * self.height)
