#python3 index.py --input /Users/bryantoblad/school/5700/hw4/input.txt --output /Users/bryantoblad/school/5700/hw4/output.txt
import argparse
from board import Board
from solver import Solver

parser = argparse.ArgumentParser(description='Solve a sudoku puzzle')
parser.add_argument('--output', help='Path to the output sudoku solution')
parser.add_argument('--input', help='Path to the input sudoku puzzle')
args = parser.parse_args()

if __name__ == '__main__':
  with open(args.input) as fp:
    lines = fp.read().split("\n")
  charactors = lines[1].split(" ")
  boardBoxes = [line.split(" ") for line in lines[2:len(charactors) + 2]] 
  board = Board(lines[0], charactors, boardBoxes)
  solver = Solver()
  solver.solve(board)
