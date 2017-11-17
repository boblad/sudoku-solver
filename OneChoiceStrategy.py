from Strategy import Strategy

class OneChoiceStrategy(Strategy):
  def __init__(self):
    pass

  def attempt(self, board):
    value_set = True
    while value_set == True:
      value_set = False
      for r in board.cells:
        for c in r:
          if c.value == '-':
            if len(c.row_group) == 1:
              value_set = True
              c.value = c.row_group[0]
              c.update(board)
            elif len(c.col_group) == 1:
              value_set = True
              c.value = c.col_group[0]
              c.update(board)
            elif len(c.region_group) == 1:
              value_set = True
              c.value = c.region_group[0]
              c.update(board)
      board.update_cells()
