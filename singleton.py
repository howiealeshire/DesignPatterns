from singleton_decorator import Singleton

'''
Singleton - "Ensure a class only has one instance, and provide a global point of access to it."

Motivation:
Sometimes, we want only one instance of a class e.g. a filesystem, a window manager, etc. 
We also want that instance to be easily accessible. Making it a global variable helps, but doesn't 
prevent other instances from being created. 

The solution is to make the class responsible for tracking its only instance, and intercepting 
requests to instantiate it, keeping it at one instance and preventing others from being created. 

Also note that some consider this an anti-pattern (Kehang actually told me that its an anti-pattern). 
See https://stackoverflow.com/questions/137975/what-are-drawbacks-or-disadvantages-of-singleton-pattern

Implementation: Look to singleton_decorator for creating a singleton. 

Singleton is classified as a creational pattern - a set of patterns for abstracting away the 
instantiation of objects. 
'''

@Singleton
class MazeFactory:
    def __init__(self):
        pass

