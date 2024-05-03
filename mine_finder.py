from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://minesweeper.online/new-game/ng')

cols = 30
rows = 16

grid = [[0]*cols for _ in range(rows)]

delay = 100 # seconds
try: 
    el =WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'level_select_13')))
except TimeoutException:
    print("page took too long to load...")
    quit()
el.click()
time.sleep(2) 
el = driver.find_element(By.CLASS_NAME,"start")
start_id = el.get_attribute("id")
start_row = ""
start_col = ""
flag_ = 0 
for x in start_id:
    if(x == '_'):
       flag_ +=1
       continue
    if(flag_== 1):
        start_col += x
    if(flag_==2):
        start_row +=x
    
start_col = int(start_col)
start_row = int(start_row)
el.click()


def updateGrid(arr):
    for i in range(rows):
        for j in range(cols):
            x_index = str(j)
            y_index = str(i)
            # print("cell_"+x_index+"_"+y_index)
            el = driver.find_element(By.ID,"cell_"+x_index+"_"+y_index)
            # print(el.get_attribute('class').split())
            class_list = el.get_attribute('class').split()
            # print(class_list)
            if 'hd_type1' in class_list:
                arr[i][j] = 1
            elif 'hd_type2' in class_list:
                arr[i][j] = 2
            elif 'hd_type3' in class_list:
                arr[i][j] = 3
            elif 'hd_type4' in class_list:
                arr[i][j] = 4
            elif 'hd_type5' in class_list:
                arr[i][j] = 5
            elif 'hd_type6' in class_list:
                arr[i][j] = 6
            elif 'hd_type7' in class_list:
                arr[i][j] = 7
            elif 'hd_type8' in class_list:
                arr[i][j] = 8  
            elif 'hd_type0' in class_list:
                arr[i][j] = -1
            elif 'hd_type10' in class_list:
                arr[i][j] = 10
            elif 'hd_type11' in class_list:
                arr[i][j] = 11
            elif 'hd_flag' in class_list:
                arr[i][j] = 13
            elif 'hd_type12' in class_list:
                arr[i][j] = 12
                

def printGrid(arr):
    line_length = cols * 3 + 1 
    print("-"*line_length)
    for i in range(rows):
        for j in range(cols):
            print("{:2}".format(arr[i][j]), end=" ") 
        print("\n")
    print("-"*line_length)
    

def dfs(arr,i,j,visited,border):
    flag = False
    if(i+1<rows):
        if(arr[i+1][j]==0):
            flag = True
    if(i-1<rows):
        if(arr[i-1][j]==0):
            flag = True
    if(j+1<cols):
        if(arr[i][j+1]==0):
            flag = True
    if(j-1<cols):
        if(arr[i][j-1]==0):
            flag = True
    if(i+1<rows and j+1<cols):
        if(arr[i+1][j+1]==0):
            flag = True
    if(i+1<rows and j-1<cols):
        if(arr[i+1][j-1]==0):
            flag = True
    if(i-1<rows and j+1<cols):
        if(arr[i-1][j+1]==0):
            flag = True                 
    if(i-1<rows and j-1<cols):
        if(arr[i-1][j-1]==0):
            flag = True
    if(flag):
        border.append([i,j])
    visited[i][j] = True
    if(i+1<rows):
        if(visited[i+1][j]==False and arr[i+1][j]!=0):
            dfs(arr,i+1,j,visited,border)
    if(i-1<rows):
        if(visited[i-1][j]==False and arr[i-1][j]!=0):
            dfs(arr,i-1,j,visited,border)
    if(j+1<cols):
        if(visited[i][j+1]==False and arr[i][j+1]!=0):
            dfs(arr,i,j+1,visited,border)
    if(j-1<cols):
        if(visited[i][j-1]==False and arr[i][j-1]!=0):
            dfs(arr,i,j-1,visited,border)
    if(i+1<rows and j+1<cols):
        if(visited[i+1][j+1]==False and arr[i+1][j+1]!=0):
            dfs(arr,i+1,j+1,visited,border)
    if(i+1<rows and j-1<cols):
        if(visited[i+1][j-1]==False and arr[i+1][j-1]!=0):
            dfs(arr,i+1,j-1,visited,border)                        
    if(i-1<rows and j+1<cols):
        if(visited[i-1][j+1]==False and arr[i-1][j+1]!=0):
            dfs(arr,i-1,j+1,visited,border)                       
    if(i-1<rows and j-1<cols):
        if(visited[i-1][j-1]==False and arr[i-1][j-1]!=0):
            dfs(arr,i-1,j-1,visited,border)

def findMines(arr,seed):
    #  checks if number of empty cells around a cell equals to number of flags to be placed. If true places those flags
     border = []
     visited = [[False]*cols for _ in range(rows)]
     dfs(arr,seed[0],seed[1],visited,border)
     for [i,j] in border:
            if(arr[i][j]>=1 and arr[i][j]<=8):
                num = arr[i][j]
                clicks = []
                if(i+1<rows):
                    if(arr[i+1][j]==0):
                        clicks.append([i+1,j])
                    if(arr[i+1][j]==13):
                        num-=1
                if(i-1<rows):
                    if(arr[i-1][j]==0):
                        clicks.append([i-1,j])
                    if(arr[i-1][j]==13):
                        num-=1
                if(j+1<cols):
                    if(arr[i][j+1]==0):
                        clicks.append([i,j+1])
                    if(arr[i][j+1]==13):
                        num-=1
                if(j-1<cols):
                    if(arr[i][j-1]==0):
                        clicks.append([i,j-1])
                    if(arr[i][j-1]==13):
                        num-=1
                if(i+1<rows and j+1<cols):
                    if(arr[i+1][j+1]==0):
                        clicks.append([i+1,j+1])
                    if(arr[i+1][j+1]==13):
                        num-=1
                if(i+1<rows and j-1<cols):
                    if(arr[i+1][j-1]==0):
                        clicks.append([i+1,j-1])
                    if(arr[i+1][j-1]==13):
                        num-=1
                if(i-1<rows and j+1<cols):
                    if(arr[i-1][j+1]==0):
                        clicks.append([i-1,j+1])
                    if(arr[i-1][j+1]==13):
                        num-=1
                if(i-1<rows and j-1<cols):
                    if(arr[i-1][j-1]==0):
                        clicks.append([i-1,j-1])
                    if(arr[i-1][j-1]==13):
                        num-=1
                if(len(clicks)==num):
                    for k in range(len(clicks)):
                        arr[clicks[k][0]][clicks[k][1]] = 13
                        el = driver.find_element(By.ID,"cell_"+str(clicks[k][1])+"_"+str(clicks[k][0]))
                        actionChains = ActionChains(driver)
                        actionChains.context_click(el).perform()
                        # el.click()
    # checks if flags around a cell equals to cell value. If true clicks the cell to reveal surrounding cells.
     for [i,j] in border:
            if(arr[i][j]>=1 and arr[i][j]<=8):
                flag_count = 0
                if(i+1<rows):
                    if(arr[i+1][j]==13):
                        flag_count+=1
                if(i-1<rows):
                    if(arr[i-1][j]==13):
                        flag_count+=1
                if(j+1<cols):
                    if(arr[i][j+1]==13):
                        flag_count+=1
                if(j-1<cols):
                    if(arr[i][j-1]==13):
                        flag_count+=1
                if(i+1<rows and j+1<cols):
                    if(arr[i+1][j+1]==13):
                        flag_count+=1
                if(i+1<rows and j-1<cols):
                    if(arr[i+1][j-1]==13):
                        flag_count+=1
                if(i-1<rows and j+1<cols):
                    if(arr[i-1][j+1]==13):
                        flag_count+=1
                if(i-1<rows and j-1<cols):
                    if(arr[i-1][j-1]==13):
                        flag_count+=1
                if(flag_count == arr[i][j]):
                    el = driver.find_element(By.ID,"cell_"+str(j)+"_"+str(i))
                    el.click()
updateGrid(grid)
printGrid(grid)
i=0
while True:
    updateGrid(grid)
    print("move: ",i)
    i+=1
    findMines(grid,[start_row,start_col])
    printGrid(grid)