#Jacob Berman
#CSCI 4448 Problem 4
#Date: 02/01/2019
#Shapes

class Shape:
    def __init__(self, x, y, z):
        self.cords = (x,y,z)
        self.z = z
        self.shapeName = None
    def getZ(self):
        return self.z
    def displayShape(self):
        s = "There is a " + str(self.shapeName) + ' at ' + str(self.cords)
        return s
    
class Circle(Shape):
    def __init__(self, x, y, z, r):
        Shape.__init__(self, x, y, z)
        self.r = r
        self.shapeName = "Cirlce"
    def displayShape(self):
        s = Shape.displayShape(self)
        s += ' of radius ' + str(self.r)
        print(s)
        
class Triangle(Shape):
    def __init__(self, x, y, z, h):
        Shape.__init__(self, x, y, z)
        self.h = h
        self.shapeName = "Triangle"
    def displayShape(self):
        s = Shape.displayShape(self)
        s += ' of height ' + str(self.h)
        print(s)
        
class Square(Shape):
    def __init__(self, x, y, z, l):
        Shape.__init__(self, x, y, z)
        self.l = l
        self.shapeName = "Square"
    def displayShape(self):
        s = Shape.displayShape(self)
        s += ' of length ' + str(self.l)
        print(s)

def sortZ(shape):
    return shape.getZ()

def displayInfo():
    db = [Circle(5, 10, 8, 2), 
    		Triangle(5, 10, 12, 10), 
    			Triangle(15, 20, 4, 8), 
    				Square(25, 30, 32, 28), 
    					Circle(17, 20, 15, 11)]
    numShapes = len(db)
    print("Number of shapes in the database:", (numShapes))
    
    db.sort(key=sortZ)
    
    for shape in db:
        shape.displayShape()

displayInfo()