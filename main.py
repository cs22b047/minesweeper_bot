import pyautogui
import cv2
import time
from PIL import Image
from PIL import ImageGrab
import numpy as np
from classifier import ImgRecognizer
from solver import Solver

# time.sleep(2)
cols = 30
rows = 16
def printGrid(arr):
    line_length = cols * 3 + 1 
    print("-"*line_length)
    for i in range(rows):
        for j in range(cols):
            print("{:2}".format(arr[i][j]), end=" ") 
        print("\n")
    print("-"*line_length)

board_box = (17,181,1730,1093)
# board_box = (332,96,1421,1188)
tile_size = ((board_box[2]-board_box[0])/cols,(board_box[3]-board_box[1])/rows)
pyautogui.click(x=board_box[0]+4.5*tile_size[0],y=board_box[1]+4.5*tile_size[1],duration=2)
pyautogui.moveTo(x=10,y=10)
recognizer = ImgRecognizer()
# img = pyautogui.screenshot()
# img = Image.open('board.png')

game_board = np.zeros((rows,cols), dtype=np.int32)
# game_board = [[0]*cols for _ in range(rows)]
recognizer.train()
solver = Solver(rows,cols,board_box,tile_size)
i=0
game_state = True
still_state = 0
while True:
    i+=1
    img = ImageGrab.grab()
    # img = pyautogui.screenshot()
    img = img.crop(board_box)
    for y in range(rows):
        for x in range(cols):
            cell_box = (x*tile_size[0], y*tile_size[1], (x+1)*tile_size[0], (y+1)*tile_size[1])
            cell = img.crop(cell_box)
            cell_val = recognizer.predict(cell)
            if cell_val==9:
                quit()
            game_board[y][x] = cell_val
    if not solver.findMines(game_board,[4,4]):
        still_state+=1
    if still_state>3:
        break
    pyautogui.moveTo(x=10,y=10)
    printGrid(game_board)
print("moves: "+str(i))