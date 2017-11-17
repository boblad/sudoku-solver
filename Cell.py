class Cell:
  def __init__(self, value, row, col):
    self.value = value
    self.row = row
    self.col = col
    self.row_group = []
    self.col_group = []
    self.region_group = []
    self.common_values = []
  
  def set_row_group(self, board):
    self.row_group = board.charactor_options[:]
    for i in board.cells[self.row]:
      if i.value != '-' and i.value not in self.row_group:
        board.set_unsolvable()
      elif i.value in board.charactor_options:
        self.row_group.remove(i.value)

  def set_col_group(self, board):
    self.col_group = board.charactor_options[:]
    for i in board.cells:
      if i[self.col].value != '-' and i[self.col].value not in self.col_group:
        board.set_unsolvable()
      elif i[self.col].value in board.charactor_options:
        self.col_group.remove(i[self.col].value)

  def set_region_group(self, board):
    row_step = int(self.row / board.region_size) * board.region_size
    col_step = int(self.col / board.region_size) * board.region_size
    self.region_group = board.charactor_options[:]
    for i in range(board.region_size):
      for j in range(board.region_size):
        if board.cells[i + row_step][j + col_step].value in self.region_group:
          self.region_group.remove(board.cells[i + row_step][j + col_step].value)

  def set_common_values(self):
    common_keys = set(self.row_group) - (set(self.row_group) - set(self.col_group))
    common_keys = list(common_keys - (common_keys - set(self.region_group)))
    self.common_values = common_keys[:]

  def print_all_cells(self, board):
    for i in board.cells:
      for j in i:
        j.print_cell()

  def print_cell(self):
    print("Cell ", self.row, self.col)
    if self.value == '-':
      print("    Row Options: ", self.row_group)
      print("    Col Options: ", self.col_group)
      print("    Region Options: ", self.region_group, "\n\n")
    else:
      print("    Value: ", self.value, "\n\n")

  def update(self, board):
    if self.value == '-':
      self.set_row_group(board)
      self.set_col_group(board)
      self.set_region_group(board)
      self.set_common_values()