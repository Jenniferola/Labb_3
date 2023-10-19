
from Circle import Circle
from Rectangle import Rectangle

def test_rectangle_area():
    my_rectangle = Rectangle(0,0,3,4)
    assert my_rectangle.area == 12

def test_rectangle_perimeter():
    my_rectangle = Rectangle(0,0,4,6)
    assert my_rectangle.perimeter == 20
    
def test_circle_area():
    my_circle = Circle(0,0,1)
    assert my_circle.area == 3.141592653589793
    
def test_circle_perimeter():
    my_circle = Circle(0,0,1)
    assert my_circle.perimeter == 6.283185307179586

def test_circle_translate_x_position():
    my_circle = Circle(1,2,1)
    assert my_circle.x_position == 1

def test_circle_translate_y_position():
    my_circle = Circle(1,2,1)
    assert my_circle.y_position == 2




        


    

    
    

