from creational_base_classes import Door, Room, Wall, Direction


class MazeFactory:
  def make_maze(self):
      return MazeFactory()
  def make_wall(self):
      return Wall()
  def make_room(self, n):
      return Room(n)
  def make_door(self,r1,r2):
      return Door(r1,r2)

class MazeGame:
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
