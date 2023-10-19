from Geometry_shapes import Geometry_shapes
import matplotlib.pyplot as plt
import math

class Circle(Geometry_shapes):
    
    def __init__ (self, x_position, y_position, radius = None):
        super().__init__(x_position, y_position)
        self.radius = radius
        
    @property
    def area(self):
        """returns area of a circle """
        return (self.radius**2) * math.pi

    @property
    def perimeter(self):
        """Returnes the perimeter of a circle """
        return (self.radius * 2) * math.pi
    
    def is_unit_circle(self):
        if self.x_position == 0 and self.y_position == 0 and self.radius == 1:
            print(f"True")
        else:
            print(f"no")

    def draw_shapes(self,shape):
     
            """Draw geometry_shapes in matplotlib """
            plt.title("Geometry shapes")
            plt.xlabel("x-coordinates")
            plt.ylabel("y-coordinates")

            plt.axis([0, 15, 0, 15])
            plt.axis("equal")

            plot_cirkel1 =plt.Circle((self.x_position, self.y_position), radius= self.radius, color = "green", alpha =.4)
            plot_cirkel2 =plt.Circle((shape.x_position, shape.y_position), radius=shape.radius, color = "red", alpha =.3)
            plot_testcircle = plt.Circle((7, 5), radius= 0.1, color = "black", alpha =.9)

            plt.gca().add_artist(plot_cirkel1)
            plt.gca().add_artist(plot_cirkel2)
            plt.gca().add_artist(plot_testcircle)

            
    def is_inside_circle(self, x_testpoint, y_testpoint):
        circle_equation = (x_testpoint - self.x_position) **2 + (y_testpoint - self.y_position) **2
        circle_equation = circle_equation**2   
        
        if circle_equation <= self.radius:
            print("True")
        else:
            print("False")
        

    def __str__(self):
        """String representation of an object for a user"""
        return f"coordinates = ({self.x_position},{self.y_position}) and the radius {self.radius}"
        

    def __repr__(self):
        """String representation an object for a programmer"""
        return f"coordinates= ({self.x_position},{self.y_position}), radius={self.radius})"
        

    def __eq__(self,other):
        """overload of == to check if the radius of two circles are the same. False if compared with a rectangle."""
        try:
            return self.radius == other.radius
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



    

