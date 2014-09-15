from numpy import * 

class GameBoard(object):
    def __init__(self, board):
        cell=[None]
        self.board=[]

    def create_block(self, cell):
        block=tile(cell, (3,3))
        return block

    def create_board(self, cell):
        board=[]
        for i in range(9):
            board.append(create_block(cell))
        return board

    def display_board(self, matrix_block):
        rows=len(matrix_block)
        cols=len(matrix_block[0])
        for row in range(0,rows,1):
            for col in range(0,cols,1):
                print matrix_block[row][col],
            print

    def check_blocks(self, num):
        ## if num in block returns true
        for cell in self.board:
            if cell==num:
                return True

    def check_rows(self, num):
        ## if num in row returns true
        pass

    def check_cols(self, num):
        ## if num in col returns true
        pass

    def check_bard(self, num):
        ## if num in block, col, and row returns true
        if check_rows and check_rows:
            return True

class Cell(object):
    def __init__(self, cell, board):
        self._cell=[]
        self._board = GameBoard()

    def check_cell(self, cell_contents=None):
        ## checks to see if cell is empty
        ## if cell is empty, returns index of cell
        for cell_contents in self._board:
            if cell_contents==None:
                return True
            else:
                return False

    def get_empty_cell_index(self):
        if self.check_if_empty:
            for cell in self._board:
                index=self._board.index(cell)
        return index

    def input_num_in_cell(self, input_num):
        ## places number in put_num_in_cell
        num=input(input_num)
        if self.check_if_num_in_cell(input_num):
            get_empty_cell_index()
        pass

    def check_if_num_in_cell(self, num):
        ## checks cell and returns True if number in cell
        if check_cell(num):
            return True
        else:
            return False

    def add_notes(self):
        ## creates an array of possible numbers for a given cell
        notes=[]
        for cell in self.board:
            for i in range(1, 10):
                if not self.board.check_board(i):
                    notes.append(i)
            self.cell.append(notes)



def create_cell_array(size):
    return [None]* size
def create_block(rows, cols):
    block = create_cell_array(rows)
    for i in range(rows):
        block[i]=create_cell_array(cols)
    return block
def create_board(block):
    board=tile(block, ())
    for i in range(3):
        for j in range(3):
            board.append(block)
    return board

    def print_board(board):
        cell_num=[]
        for row in board: #block level
            for cell in row: #row
                for  sub_item in cell:
                    num.append(sub_item)
        step=3
        for i in range(16):
            if i%2 == 0:
                print ("---------------------------------------")
            for j in range(step):
                print("| {} {} {} || {} {} {} || {} {} {} |" .format(num[i+j]))
>>> cell=create_cell_array(3)
>>> cell
[None, None, None]
>>> from numpy import *
>>> tile(cell, (3,1))
array([[None, None, None],
       [None, None, None],
       [None, None, None]], dtype=object)
>>> def create_block(rows, cols):
...     block = create_cell_array(rows)
...     tile(block, (3,1))
...     return block
... 
>>> cell=create_cell_array(3)
>>> cell
[None, None, None]
