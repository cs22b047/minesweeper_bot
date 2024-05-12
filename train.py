import pyautogui
import cv2
import time
from PIL import Image
from PIL import ImageGrab
import numpy as np
from classifier import ImgRecognizer
from solver import Solver

time.sleep(2)

board_box = (17,181,1730,1093)
tile_size = ((board_box[2]-board_box[0])/30,(board_box[3]-board_box[1])/16)
pyautogui.moveTo(x=10,y=10)
recognizer = ImgRecognizer()
cols = 30
rows = 16
img = ImageGrab.grab()
img = img.crop(board_box)
x=int(input("x:"))
y=int(input("y:"))
cell_box = (x*tile_size[0], y*tile_size[1], (x+1)*tile_size[0], (y+1)*tile_size[1])
cell = img.crop(cell_box)
cell.save('Training_data2/four/2.png')
