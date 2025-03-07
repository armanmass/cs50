from minesweeper import *

ms = Minesweeper()

for row in ms.board:
    for cell in row:
        print(cell)

