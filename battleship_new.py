#battleship.py

class Ship(object):
    def __init__(self, length):
        #creates ship
        self._length = length
        self._health = []
        for i in range(0, length):
            self._health.append(1.0)

    def get_length(self):
        return self._length

    length = property(get_length)

    def take_damage(self, index, damage=1.0):
        #applies damage to that index of ship
        # if damage is greater than the health of the ship at the index, set health to 0.0
        if self.get_health_at(index) < damage:
            self._health = 0.0
        else:
            self._health = damage
        return self._health
     
    def get_health(self):
        #returns fraction of the health of the ship
        # Returns health of entire ship
        #   returns: float between 0.0 and 1.0
        return sum(self._health)/float(length)
    
    health = property(get_health)

    def get_health_at(self, index):
        # Returns health of ship segment 'index'
        #   returns: float between 0.0 and 1.0
        return self._health[index]

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise TypeError
        return Point(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        return Point(self.x*other, self.y*other)

class GameBoard(object):
    def __init__(self, width, height):
        #creates board from double array
        self._width = width
        self._height = height
        self._board = [[None for y in range(self._height)] for x in range(self._width)]
        self._ships = []
        pass

    @staticmethod
    def _delta_for_direction(direction):
        """Returns delta (dx, dy) for given direction
        raises ValueError if direction not recognized
        """
        if direction == 'n':
            return Point(0, -1)
        elif direction == 's':
            return Point(0, 1)
        elif direction == 'e':
            return Point(1, 0)
        elif direction == 'w':
            return Point(-1, 0)
        else:
            raise ValueError('bad direction: {}'.format(str(direction)))

    def place_ship(self, ship, x, y, direction):
        #create empty tuple of ship coordinates and index hit
        # Places a ship with its head at coordinate (x,y) and facing the given direction (one of 'n', 's', 'e', 'w')
        #   if succesful: returns True
        #   if ship collision: returns False
        #   if ship out of bounds: raises IndexError
        if not self.can_place_ship(ship, x, y, direction):
            return False
        self._ships.append(ship)
        # at this point, i know i can place the ship
        delta = GameBoard._delta_for_direction(direction)
        c = Point(x, y)
        for i in range(0, ship.length):
            self._board[c.x][c.y] = (ship, i)
            c = c - delta
        return True

    def lookup(self, x, y):
        # do not need to store (x,y), error if ship fall on another or it ship is placed off the gird
        #general function to compare if userinout (x,y) collides with anything (hit, miss, ship on ship, ship in grid)
        ##look up function coordinate, return what is there 
        #(ship object with index hit, tuple(ship, i)) or none, throw exception for coordinate not on board
        # Returns what's at the coordinate (x,y)
        #   if x,y out of bounds of the game board: raises IndexError
        #   if x,y is empty: returns None
        #   if x,y has a ship: returns (ship at x,y, index of ship at x,y)
        return self._board[x][y]

    def ships_remaining(self):
        #returns number of ships on the game board whose health > 0.0
        ships_remaining = 0
        for ship in self._ships:
            if ship.health > 0:
                ships_remaining = ships_remaining + 1
        return ships_remaining

    def take_damage(self, x, y, damage=1.0):
        #applies given amout of damage to coordinate (x,y)
        whats_there = self.lookup(x, y)
        if whats_there is not None:
            whats_there[0].take_damage(whats_there[1], damage)

    def can_place_ship(self, ship, x, y, direction):
        # Returns whether the given ship can be placed at (x,y) in the given direction
        #    if it can be placed: return True
        #    if it collides with another ship: return False
        #    if it is out of bounds: return False
        delta = GameBoard._delta_for_direction(direction)
        c = Point(x, y)
        for i in range(0, ship.length):
            if self._board[c.x][c.y] is not None:
                return False
            c = c - delta
        return True

    def dump(self):
        # prints out the game board
        for j in range(self._height):
            chunks = []
            for i in range(self._width):
                if self._board[i][j] is not None:
                    chunks.append('O')
                else:
                    chunks.append('X')
            print ''.join(chunks)
