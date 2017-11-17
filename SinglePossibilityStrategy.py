from Strategy import Strategy

class SinglePossibilityStrategy(Strategy):
  def __init__(self):
    pass

  def attempt(self, board):
    value_set = True
    while value_set == True:
      value_set = False
      for r in board.cells:
        for c in r:
          if c.value == '-':
            common_keys = set(c.row_group) - (set(c.row_group) - set(c.col_group))
            common_keys = list(common_keys - (common_keys - set(c.region_group)))
            if len(common_keys) == 1:
              value_set = True
              c.value = common_keys[0]
              c.update(board)
      board.update_cells()
