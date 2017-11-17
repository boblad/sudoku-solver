import math 
from Cell import Cell

class Board:
  def __init__(self, size, charactor_options, spaces):
    self.size = int(size)
    self.charactor_options = charactor_options
    self.spaces = spaces
    self.region_size = int(math.sqrt(self.size))
    self.cells = None
    self.build_cells()
    self.update_cells()
    self.is_solvable = True

  def update_cells(self):
    for r in self.cells: 
      for c in r:
        c.update(self)

  def set_unsolvable(self):
    self.is_solvable = False

  def build_cells(self):
    self.cells = []
    for s_i, s_x in enumerate(self.spaces):
      temp_cells = []
      for s_j, s_y in enumerate(s_x):
        temp_cells.append(Cell(s_y, s_i, s_j))
      self.cells.append(temp_cells)


  def has_valid_dimensions(self):
    for i in self.spaces:
      if len(i) != self.size:
        return False
    return True

  def printBoard(self):
    empty_count = 0
    for i in self.cells:
      line = ''
      for j in i:
        if j.value == '-':
          empty_count = empty_count + 1
        line = line + str(j.value) + ' '
      print(line)
    print('\nempty count: ', empty_count)
    print('\n\n')
      
