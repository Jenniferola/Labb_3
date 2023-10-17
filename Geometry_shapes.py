class Geometry_shapes:

    def __init__(self, name, x_position = None, y_position = None):
        self.name = name
        self.x_position = x_position
        self.y_position = y_position

    def translate(self, steps_x_position, steps_y_position):
        """Changes the shapes x and y coordinates"""       
        try:
            if steps_x_position > 0:
                self.x_position = self.x_position + steps_x_position
            elif steps_x_position < 0:
                self.x_position = self.x_position - steps_x_position     
       
            if steps_y_position > 0:
                self.y_position = self.y_position + steps_y_position
            elif steps_x_position < 0:
                self.y_position = self.y_position - steps_y_position
        except:
            "Wrong, please write two integears."

        print(f"({self.x_position}, {self.y_position})")
