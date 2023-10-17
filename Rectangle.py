import Geometry_shapes

class Rectangle(Geometry_shapes):

    def __init__ (self, name, x_position, y_position, side1 = None, side2= None):
        super().__init__(name, x_position, y_position)
        self.x_position = x_position
        self.y_position = y_position
        self.side1 = side1
        self.side2 = side2
           
    @property
    def area(self):
        """Returnes the area of an rectangle """
        return self.side1 * self.side2
    
    @property
    def perimeter(self):
        """Returnes the perimeter of an rectangle """
        return self.side1*2 +self.side2*2
    
    def is_square(self):
        """Checks if the rectangle is a square """
        if self.side1 == self.side2:
            print("True")
        else:
            print("False")


    def __str__(self):
        """String representation of an object for a user"""
        return f"{self.name} has got the coordinates ({self.x_position},{self.y_position}) and the sides {self.side1} and {self.side2}"
        

    def __repr__(self):
        """String representation an object for a programmer"""
        return f"{self.name}(coordinates=({self.x_position},{self.y_position}), side1={self.side1}, side2={self.side2})"
        
    
    
    #def __eq__(self,other):
        """overload of == to check equality """
        ...

   # def __lt__(self):
        """overload of < """
        ...

    #def __gt__(self):
        """overload of > """
        ...

    #def __le__(self):
        """overload of <= """
        ...
    
    #def __ge__(self):
        """overload of >= """



    