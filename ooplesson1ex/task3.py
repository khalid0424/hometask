class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius =radius
    def area(self):
        print( self.pi * (self.radius ** 2))


chen = Circle(5)
chen.area()

