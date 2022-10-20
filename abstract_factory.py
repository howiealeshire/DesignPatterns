from creational_base_classes import Door, Room, Wall, Direction

'''
Abstract Factory:
Essentially, a way to create objects (related to each other) without specifying their concrete classes.
Abstract Factory is classified as a creational pattern - a set of patterns for abstracting away the 
instantiation of objects. 
Motivation: 
    Suppose there's a UI toolkit, A.
    A supports multiple appearance (look-and-feel) standards.
    These standards have different appearances and behaviours - for use with different widgets e.g. scroll bars, windows, etc.
    Instantiating the concrete classes of these appearances makes the application inflexible - that is, 
    it's hard to change the appearance standard later (say, if you were porting to different platforms).
    Abstract Factory makes it so you don't have to worry about instantiating the concrete classes every time
    and reaching for a new one is easy.  
'''

class MazeFactory:
    # each one of these is a factory method, a way to instantiate different concrete classes
    # it's easy to create a new factory by subclassing and overriding these methods
  def make_maze(self):
      return MazeFactory()
  def make_wall(self):
      return Wall()
  def make_room(self, n):
      return Room(n)
  def make_door(self,r1,r2):
      return Door(r1,r2)

class MazeGame:
    # the main application
    def create_maze(self,factory):
        maze = factory.make_maze()
        r1 = factory.make_room(1)
        r2 = factory.make_room(2)
        door = factory.make_door(r1, r2)

        maze.make_room(r1)
        maze.make_room(r2)

        r1.set_side(Direction.North, factory.make_wall)
        r1.set_side(Direction.East, door)
        r1.set_side(Direction.South, factory.make_wall)
        r1.set_side(Direction.West, factory.make_wall)

        r2.set_side(Direction.North, factory.make_wall)
        r2.set_side(Direction.East, factory.make_wall)
        r2.set_side(Direction.South, factory.make_wall)
        r2.set_side(Direction.West, door)

        return maze


class EnchantedRoom(Room):
    _cast_spell = None
    def __init__(self, n, cast_spell):
        super().__init__(n)
        self._cast_spell = cast_spell

class DoorNeedingSpell(Door):
    def __init__(self,r1,r2):
        super().__init__(r1,r2)

class EnchantedMazeFactory(MazeFactory):
    def make_room(self,n):
        # these concrete classes come with useful defaults that the calling client doesn't have to set themselves
        # removing the burden of instantiation of certain concrete classes
        return EnchantedRoom(n, self.cast_spell())

    def make_door(self,r1,r2):
        return DoorNeedingSpell(r1,r2)

    def cast_spell(self):
        pass


class BombedWall(Wall):
    def __init__(self):
        super().__init__()


class RoomWithABomb(Room):
    def __init__(self, n):
        super().__init__(n)


class BombedMazeFactory(MazeFactory):
    def make_wall(self):
        return BombedWall()

    def make_room(self,n):
        return RoomWithABomb(n)


if __name__ == "__main__":
    game = MazeGame()
    bmf = BombedMazeFactory()
    game.create_maze(bmf)
    print(game)
