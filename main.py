import pyautogui
import cv2
import time
from PIL import Image
from PIL import ImageGrab
import numpy as np
from classifier import ImgRecognizer
from solver import Solver

time.sleep(2)

def printGrid(arr):
    line_length = cols * 3 + 1 
    print("-"*line_length)
    for i in range(rows):
        for j in range(cols):
            print("{:2}".format(arr[i][j]), end=" ") 
        print("\n")
    print("-"*line_length)

board_box = (17,181,1730,1093)
tile_size = ((board_box[2]-board_box[0])/30,(board_box[3]-board_box[1])/16)
pyautogui.click(x=board_box[0]+4*tile_size[0]+25,y=board_box[1]+4*tile_size[1]+25,duration=2)
pyautogui.moveTo(x=10,y=10)
recognizer = ImgRecognizer()
# img = pyautogui.screenshot()
# img = Image.open('board.png')
cols = 30
rows = 16
game_board = np.zeros((rows,cols), dtype=np.int32)
# game_board = [[0]*cols for _ in range(rows)]
recognizer.train()
solver = Solver()
i=0
game_state = True
while i<10:
    i+=1
    img = ImageGrab.grab()
    img = img.crop(board_box)
    for y in range(rows):
        for x in range(cols):
            cell_box = (x*tile_size[0], y*tile_size[1], (x+1)*tile_size[0], (y+1)*tile_size[1])
            cell = img.crop(cell_box)
            cell_val = recognizer.predict(cell)
            if cell_val==9:
                game_state = False
                break
            game_board[y][x] = cell_val
    if not game_state:
        break
    solver.findMines(game_board,[4,4])
    pyautogui.moveTo(x=10,y=10)
    printGrid(game_board)