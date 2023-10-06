class Geometry_shapes:

    def __init__(self, area, perimeter, x_position, y_position):
        self.area = area
        self.perimeter = perimeter
        self.x_position = x_position
        self.y_position = y_position
        
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, number):
        self._area = number

## Fortsättning skriv properties för andra init paramterar efter area. Döp dem till 0 som grundvärde för objekten. Fråga hur man ska göra. 


my_circle = Geometry_shapes(0)

print(my_circle.area)