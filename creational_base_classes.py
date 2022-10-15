import abc
from enum import Enum, auto


class Direction(Enum):
    North = 0
    South = 1
    East = 2
    West = 3

class MapSite:
    @abc.abstractmethod
    def enter(self):
        pass

class Side:
    north = None
    east = None
    south = None
    west = None

class Room(MapSite):

    _sides = Side()
    _room_no = 0

    def __init__(self, room_no):
        self._room_no = room_no
    def get_side(self,direction):
        pass
    def set_side(self,direction,map_site):
        if direction == 0:
            self._sides.north = map_site
        if direction == 1:
            self._sides.south = map_site
        if direction == 2:
            self._sides.east = map_site
        if direction == 3:
            self._sides.west = map_site
    def enter(self):
        return super(Room,self).enter()

class Wall(MapSite):
    def enter(self):
        return super(Wall,self).enter()

class Door(MapSite):
    def __init__(self,room1,room2):
        self._room1 = room1
        self._room2 = room2

    def enter(self):
        return super(Door,self).enter()

    def other_side_from(self,room):
        return room

class Maze:
    def add_room(self,room):
        pass
    def room_no(self, room_num):
        return Room(room_num)









