#filename: battleship.py

class BattleShip:

    # front of ship part[0], part[1], part[2]... part[length-1]   back of ship

    def __init__(self, length): # create ship with given length
        self._length = length
        self._health = []
        for i in range(0, length):
            self._health.append(1.0)

    def get_length(self):
        return self._length

    length = property(get_length)

    def take_damage(self, index):
        self._health[index] = 0.0

    def get_health(self):
        # returns fraction of ship damaged (0.0 sunk, 1.0 fine)
        return sum(self._health)/float(length)

class Gameboard: #hit or miss, records the hit position
    def __init__(self, width, height):
        self._wdith = width
        self._height = height

    def place_ship(self, ship, x, y, direction):
        # place head of ship at (x,y) and have it face the given direction
        # throw exception if ship placed out of bounds of game board
        self._ship = ship
        self._x = x
        self._y = y
        self._direction = direction
        user_input = new_input("enter direction of ship (n, e, s, w): ")
        s =[]
        try:
            if self._direction == "n":
                if length + self._y > self._height:
                    raise Exception ("invalid placement")
                for i in range(0, length):
                    s.append([self._x, self._y + i])
            if self._direction == "e":
                if length + self._x > self._width:
                    raise Exception ("invalid placement")
                for i in range(0, length):
                    s.append([self._x + i, self._y])
            if self._direction == "s":
                if self._y - length < 0:
                    raise Exception ("invalid placement")
                for i in range(0, length):
                    s.append([self._x, self._y - i]) 
            if self._direction == "w":
                if self._x - length < 0:
                    raise Exception ("invalid placement")
                for i in range(0, length):
                    s.append([self._x - i, self._y])
            except ValueError:
                print "enter valid ship placement"
        self._ship = s # nested list of ship coordinates

    def fleet_health(self, x, y):
        self._x = x
        self._y = y
        ships_remaining = 0
        if length == check_hit(self, x, y):
            ship_destroyed = True
            ships_remaining += 1
        if ships_remaining == 5
            print "Game Over!"
        pass

    def check_hit(self, x, y):
        self._hits = 0
        misses_list = []
        hits_list = []
        cor = [[x, y]]

        for i in cor:
            for j  in self._ship:
                if cor[i] == self._ship[j]
                    hits_list.append(j)
                    self._hit += 1
                else:
                    misses_list.append(i)
        return self._hits

    def print_board(self): # print board
        self._board = [[0 for x in range(10)] for y in range(10)]
