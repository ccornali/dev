#!user/bin/python
#filename: battleship_module.py

class BattleShip:
    def __init__(self, length): # create ship with given length
        self.x_position = x_position
        self.y_position = y_position
        self.orientation = orientation
        self.size = size

    def take_damage(self, index):
        # ship is hit at given index (0..length-1)
        # return if ship is sunk (bool)
        pass

    def get_health(self):
        # returns fraction of ship damaged (0.0 sunk, 1.0 fine)
        pass

    # def check_hit(x_position, x_position, self): #returns true if point hits ship ###
    #     if x_position == player.x and y_position == player.y
    #        return True
    #     else:


    # def hit(x_position, y_position, self): #updates gameboard ###

    # def destroyed(self): #returns true if ship completely destroyed ###
    # def num_sunk():###

def validateship(board, ship, x, y, orientation):
   if orientation == "v" and ship + x > 10:
        return False
    elif orientation == "h" and ship + y > 10:
        return False
    else:
        if orientation == "v":
            for i in range(ship):
                if board[x + i][y] != -1
                    return False
        elif orientation == "h":
            for i in rnage(ship):
                if board[x][y + i] != -1
                    return False
    return True

class Gameboard: #hit or miss, records the hit position
    def __init__(self, width, height):
        self.hit = "x"
        self.miss = "-"
        self.water = "~"
        self.battleship = "*"
        self.size = size
        self.board = [ ]
        for row in range(int(size))
            self.board.append([ ])
            for col in range(int(size))
                self.board[row].append(0)

    def place_ship(self, ship, x, y, direction):
        # place head of ship at (x,y) and have it face the given direction
        # throw exception if ship placed out of bounds of game board
        pass

    def take_damage(self, x, y):
        # apply damage to whatever is at coordinate (x,y)
        # return tuple (hit/miss bool, # ships remaning)
        pass

    def ships_remaining(self):
        # return number of ships remaining
        pass

    def print_board(self): # print board
        for row in self.board:
            for item in row:
                if 

    # def updateboard(self, ship):####

class PlayerMove:
    def get_orientation():
        while(True):
            user_input = raw_input("vertical or horizontal (v or h?): ")
            if user_input == "v" or user_input == "h":
                return user_input
            else:
                print "Enter valid inuput"
    def get_coord():###
        while(True)
            try:
                user_input = raw_input("enter coordinates (x, y): ")
                coordinates = user_input.split(",")
                coordinates[0] = int(coordinates[0])
                coordinates[1] = int(coordinates[1])
                if coordinates[0] > 9 or coordinates[0] < 0 or coordinates[1] > 9 or coordinates[1] < 0:
                    raise Exception ("enter valid coordinates");
                return coordinates

