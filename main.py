import pyautogui
import time
import numpy as np
from classifier import ImgRecognizer
from solver import Solver

# time.sleep(2)
cols = 30
rows = 16
def printGrid():
    line_length = cols * 3 + 1 
    print("-"*line_length)
    for i in range(rows):
        for j in range(cols):
            print("{:2}".format(game_board[i][j]), end=" ") 
        print("\n")
    print("-"*line_length)

def get_board():
    img = pyautogui.screenshot()
    img = img.crop(board_box)
    flag_count = 0
    for y in range(rows):
        for x in range(cols):
            cell_box = (x*tile_size[0], y*tile_size[1], (x+1)*tile_size[0], (y+1)*tile_size[1])
            cell = img.crop(cell_box)
            cell_val = recognizer.predict(cell)
            if(cell_val==13):
                flag_count+=1
            if cell_val==9:
                print(solver.num_guesses)
                quit()
            game_board[y][x] = cell_val
    if flag_count>=99:
        solver.findMines(game_board,[4,4])
        print(solver.num_guesses)
        quit()
    

board_box = (17,181,1730,1093)
tile_size = ((board_box[2]-board_box[0])/cols,(board_box[3]-board_box[1])/rows)
pyautogui.click(x=board_box[0]+4.5*tile_size[0],y=board_box[1]+4.5*tile_size[1],duration=2)
pyautogui.moveTo(x=10,y=10)
recognizer = ImgRecognizer()

game_board = np.zeros((rows,cols), dtype=np.int32)
# game_board = [[0]*cols for _ in range(rows)]
recognizer.train()
solver = Solver(rows,cols,board_box,tile_size)
i=0
game_state = True
still_state = 0
while True:
    i+=1
    get_board()
    solver.findMines(game_board,[4,4])
    pyautogui.moveTo(x=10,y=10)
    # printGrid(game_board)