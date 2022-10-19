
class Manipulator:
    pass

class TextManipulator:
    pass

class Shape:
    bottom_left = (0,0)
    top_right = (0,0)
    def set_bounding_box(self,bottom_left,top_right):
        self.bottom_left = bottom_left
        self.top_right = top_right
    def create_manipulator(self):
        return Manipulator()

class TextView:
    empty = False
    def get_origin(self,x,y):
        pass
    def get_extent(self,width,height):
        pass
    def is_empty(self):
        return self.empty

class TextShape(Shape,TextView):
    bottom_left = (0,0)
    top_right = (0,0)
    def set_bounding_box(self,bottom_left,top_right):
        bottom, left, width, height = 0, 0, 0, 0
        super(TextShape,self).get_origin(bottom,left)
        super(TextShape,self).get_extent(width,height)
        self.bottom_left = (bottom,left)
        self.top_right = (bottom + height, left + width)
    def is_empty(self):
        return super(TextShape,self).is_empty()
    def create_manipulator(self):
        return TextManipulator()





