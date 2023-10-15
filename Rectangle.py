class Rectangle:

    def __init__ (self, side1 = None, side2 = None, x_position = None, y_position = None):
        self.side1 = side1
        self.side2 = side2
        self.x_position = x_position
        self.y_position = y_position
        
    @property
    def area(self):
        """Returnes the area of an rectangle """
        return self.side1 * self.side2
    
    @property
    def perimeter(self):
        """Returnes the perimeter of an rectangle """
        return self.side1*2 +self.side2*2
    