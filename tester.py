import pyximport

pyximport.install()
from minesweeper import MineSweeper

if __name__ == '__main__':
    mine = MineSweeper(25, 25, 25)
    mine.draw_panel().show()
    while True:
        try:
            location = MineSweeper.parse_input(input())
            mine.mine(location[0], location[1])
            mine.draw_panel().show()
            print(mine.state)
        except Exception as e:
            print(e)