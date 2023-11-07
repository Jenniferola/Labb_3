from Circle import Circle
from Rectangle import Rectangle

circle1 = Circle(x_position=0, y_position=0, radius = 1)

circle2 = Circle(x_position=1, y_position=1, radius = 1)

rectangle = Rectangle(x_position=0, y_position=0, width= 1, height= 1)

print(circle1 == circle2)

print(circle1 == rectangle)

circle1.is_inside_circle(2,2)

circle1.is_inside_circle(0.5,0.5)

rectangle.is_inside_rectangle(0.5,0.5)

circle1.translate(3,6)

rectangle.is_square()

print(rectangle)

print(repr(rectangle))

print(circle1 < circle2)

circle1.draw_shapes(circle2)





