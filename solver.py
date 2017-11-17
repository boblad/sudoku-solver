import time
from OneChoiceStrategy import OneChoiceStrategy
from SinglePossibilityStrategy import SinglePossibilityStrategy
from GuessStrategy import GuessStrategy

class Solver:
  def __init__(self):
    self.start_time = None
    self.end_time = None
    self.one_choice_strategy = OneChoiceStrategy()
    self.single_possibility_strategy = SinglePossibilityStrategy()
    self.guess_strategy = GuessStrategy()

  #Method to be overriden
  def print_time_results(self): pass

  #Method to be overriden
  def complete(self): pass

  def start_timer(self):
    self.start_time = time.time()

  def stop_timer(self):
    self.end_time = time.time()

  def get_time_results(self):
    return self.end_time - self.start_time
  
  def is_complete(self, board):
    for r in board.cells:
      for c in r:
        if c.value == '-':
          return False
    board.printBoard()
    return True

  def solve(self, board):
    if self.is_complete(board) == True or board.is_solvable == False:
      return
    self.start_timer()
    self.one_choice_strategy.attempt(board)
    self.single_possibility_strategy.attempt(board)
    board_options = self.guess_strategy.attempt(board)
    for b in board_options:
      self.solve(b)
    self.stop_timer()
