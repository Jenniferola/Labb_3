class Geometry_shapes:

    def __init__(self, x_position = None, y_position = None):
        self.x_position = x_position
        self.y_position = y_position

    def translate(self, x_position, y_position):
        """Changes the shapes x and y coordinates""" 

        try:
            self.y_position = y_position
            self.x_position = x_position

        except:
            "Wrong, please write two integears."

        print(f"({self.x_position}, {self.y_position})") 
