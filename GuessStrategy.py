from Strategy import Strategy
from copy import deepcopy

class GuessStrategy(Strategy):
  def __init__(self):
    self.most_likely_cell = None
    self.board_options = None

  def set_initial_likely(self, board):
    found = False
    for r in board.cells:
      for c in r:
        if c.value == '-':
          self.most_likely_cell = c
          found = True
          break
      if found == True:
        break
  
  def set_most_likely_cell(self, board):
    self.set_initial_likely(board)
    for r in board.cells:
      for c in r:
        if c.value == '-' and len(c.common_values) < len(self.most_likely_cell.common_values):
          found = True
          self.most_likely_cell = c

  def attempt(self, board):
    value_set = True
    self.set_most_likely_cell(board)
    if self.most_likely_cell != None:
      self.board_copies = [deepcopy(board) for mlc in self.most_likely_cell.common_values]
      for index, b in enumerate(self.board_copies):
        b.cells[self.most_likely_cell.row][self.most_likely_cell.col].value = self.most_likely_cell.common_values[index]
        b.update_cells()
      return self.board_copies
    return [board]
