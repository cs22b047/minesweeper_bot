#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[2]:


driver = webdriver.Chrome()
driver.maximize_window()


# In[3]:


driver.get('https://minesweeper.online/new-game/ng')


# In[4]:


from selenium.webdriver.common.by import By


# In[5]:


# lev3 = driver.find_element(By.CLASS_NAME, "level3-link")
# lev3.click()


# In[9]:


cols = 30
rows = 16
def updateCells(arr):
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
    print("--------------------------------------------------------------")
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j],end=" ")
        print("\n")
    print("--------------------------------------------------------------")

grid = [[0]*cols for _ in range(rows)]
# printGrid(grid)
# el = driver.find_elements(By.CLASS_NAME,"menu-link")
# el[1].click()
# time.sleep(2)


# In[10]:
delay = 1000 # seconds
time.sleep(5)
el =WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'level_select_13')))
el.click()
delay = 1000 # seconds
# el =WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'start')))
time.sleep(2) 
el = driver.find_element(By.CLASS_NAME,"start")
el.click()

# In[ ]:


from selenium.webdriver import ActionChains
def findMines(arr):
     totalClicks = 0
     for i in range(rows):
        for j in range(cols):
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
                    totalClicks+=len(clicks)
                    for k in range(len(clicks)):
                        arr[clicks[k][0]][clicks[k][1]] = 13
                        el = driver.find_element(By.ID,"cell_"+str(clicks[k][1])+"_"+str(clicks[k][0]))
                        actionChains = ActionChains(driver)
                        actionChains.context_click(el).perform()
                        # el.click()
    #  if(totalClicks==0):
    #      return False
     for i in range(rows):
        for j in range(cols):
            if(arr[i][j]>=1 and arr[i][j]<=8):
                flag_count = 0;
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
     return True
updateCells(grid)
printGrid(grid)
while True:
    updateCells(grid)
    if not findMines(grid):
        break
    printGrid(grid)

print("Finished!!")
time.sleep(100000)
# In[ ]:




