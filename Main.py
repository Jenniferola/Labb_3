import Geometry_shapes
from Circle import Circle
from Rectangle import Rectangle

circle1 = Circle("cicle1", x_position=0, y_position=0, radius = 1)

circle2 = Circle("circle2", x_position=6, y_position=6, radius = 1)

rectangle = Rectangle("rectangle", x_position=0, y_position=0, side1= 1, side2= 1)

print(circle1 == circle2)

print(circle2 == rectangle)

circle1.is_unit_circle()

circle1.translate(5,5)

rectangle.is_square()

print(rectangle)

print(repr(rectangle))

circle1.draw_shapes(circle2)

circle1.is_inside_circle(7,5)


