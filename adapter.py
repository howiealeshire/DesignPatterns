'''
Adapter - "Convert the interface of a class into another interface clients expect. Adapter lets
classes work together that couldn't otherwise because of incompatible interfaces."

Motivation:
Say you have a drawing editor (e.g. MSPaint). The main abstraction in this is the graphical object, which allows
an object to draw itself and edit its shape. Shape is the graphical object, an abstract class. You've got
LineShape, PolygonShape, ... XShape as subclasses. They have their own overridden methods of drawing themselves and editing their shapes.
Line and Polygon are rather simple to implement. However, suppose you need a TextShape class. This class comes with
considerable complexity. There's a UI toolkit that provides a TextView class which edits and displays text.
We want to reuse this, but the TextView didn't consider Shape objects in their design. Changing the underlying
implementation of TextView to satisfy TextShape is a brittle approach - other objects might depend on TextView,
and we may need the default behaviour of TextView another time.

Implementation:
A class adapter uses multiple inheritance to create the appropriate interface. From the motivating example in this case,
we use the TextView's functionality (methods) to construct the appropriate shape interface.

'''
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





