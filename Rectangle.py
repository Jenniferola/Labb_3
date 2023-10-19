from Geometry_shapes import Geometry_shapes

class Rectangle(Geometry_shapes):

    def __init__ (self, x_position, y_position, width = None, height= None):
        super().__init__(x_position, y_position)
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
    
    @property
    def area(self):
        """Returnes the area of an rectangle """
        return self.width * self.height
    
    @property
    def perimeter(self):
        """Returnes the perimeter of an rectangle """
        return self.width*2 +self.height*2
    
    def is_square(self):
        """Checks if the rectangle is a square """
        if self.width == self.height:
            print("True")
        else:
            print("False")

    def __str__(self):
        """String representation of an object for a user"""
        return f"rectangle´s coordinates are ({self.x_position},{self.y_position}), the width is {self.width} and the height is {self.height}"
        

    def __repr__(self):
        """String representation an object for a programmer"""
        return f"coordinates=({self.x_position},{self.y_position}), width={self.width}, height={self.height}"
        
    
    def __eq__(self,other):
        """overload of == to check equality """
        try:
            return self.area == other.area
        except:
            print("False")


    def __lt__(self,other):
        """overload of < """
        try:
            return self.area < other.area
        except:
            print("False")


    def __gt__(self,other):
        """overload of > """
        try:
            return self.area > other.area
        except:
            print("False")


    def __le__(self,other):
        """overload of <= """
        try:
            return self.area <= other.area
        except:
            print("False")

    
    def __ge__(self,other):
        """overload of >= """
        try:
            return self.area >= other.area
        except:
            print("False")




    