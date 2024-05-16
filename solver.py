import pyautogui
import numpy as np
class Solver:
    def __init__(self,rows,cols,board_box,tile_size):
            self.rows=rows
            self.cols=cols
            # self.board_box = (17,181,1730,1093)
            self.board_box = board_box
            self.tile_size = tile_size
            self.num_guesses = 0
            
    def neighbours(self,i,j):
        for delta_i in (-1,0,1):
            for delta_j in (-1,0,1):
                if 0<=i+delta_i<self.rows and  0<=j+delta_j<self.cols and not delta_i==delta_j==0:
                    yield i+delta_i,j+delta_j 
    def dfs(self,arr,i,j,visited,border):
        flag = False
        for ni,nj in self.neighbours(i,j):
            if arr[ni][nj]==-1:
                flag=True
        if flag:
            border.append((i,j))
        visited[i][j] = True
        for ni,nj in self.neighbours(i,j):
            if not visited[ni][nj] and 0<=arr[ni][nj]<=8:
                self.dfs(arr,ni,nj,visited,border)

    def findMines(self,arr,seed):
        total_clicks = 0
        border = []
        visited = [[False]*self.cols for _ in range(self.rows)]
        self.dfs(arr,seed[0],seed[1],visited,border)
        # print(border)   
        # return False                         
        right_clicks = []
        left_clicks = []
        for [i1,j1] in border:
            for [i2,j2] in border:
                    if i1-i2==1 or i1-i2==-1 or j1-j2==1 or j1-j2==-1:
                        s1 = set()
                        s2 = set()
                        v1 = arr[i1][j1]
                        v2 = arr[i2][j2]
                        for ni,nj in self.neighbours(i1,j1):
                            if arr[ni][nj]==-1:
                                s1.add((ni,nj))
                            if arr[ni][nj]==13:
                                v1-=1
                        
                        for ni,nj in self.neighbours(i2,j2):
                            if arr[ni][nj]==-1:
                                s2.add((ni,nj))
                            if arr[ni][nj]==13:
                                v2-=1

                        if(len(s1&s2)!=0):
                            if(v1-v2 == len(s1-s2)):
                                for tile in s1-s2:
                                    arr[tile[0]][tile[1]] = 13
                                    right_clicks.append(tile)
                                for tile in s2-s1:
                                    # arr[tile[0]][tile[1]] = -2
                                    left_clicks.append(tile)
                        elif(len(s1)==v1):
                            for tile in s1:
                                arr[tile[0]][tile[1]] = 13
                                right_clicks.append(tile)
        for tile in right_clicks:
            total_clicks+=1
            pyautogui.click(button='right',x=self.board_box[0]+(tile[1]+0.5)*self.tile_size[0],y=self.board_box[1]+(tile[0]+0.5)*self.tile_size[1])
            
        for tile in left_clicks:
            # el = driver.find_element(By.ID,"cell_"+str(tile[1])+"_"+str(tile[0]))
            # el.click()
            total_clicks+=1
            pyautogui.click(x=self.board_box[0]+(tile[1]+0.5)*self.tile_size[0],y=self.board_box[1]+(tile[0]+0.5)*self.tile_size[1])
        for [i,j] in border:
                if(arr[i][j]>=1 and arr[i][j]<=8):
                    num = arr[i][j]
                    safe = 0
                    for ni,nj in self.neighbours(i,j):
                        if arr[ni][nj]==-1:
                            safe+=1
                        if arr[ni][nj]==13:
                            num-=1
                    if num==0 and safe>=1:
                        total_clicks+=1
                        pyautogui.click(x=self.board_box[0]+(j+0.5)*self.tile_size[0],y=self.board_box[1]+(i+0.5)*self.tile_size[1])
        if(total_clicks==0):
            self.num_guesses+=1
            self.guess(border,arr)
   
    def guess(self,border,arr):
        probability = np.zeros((self.rows,self.cols),dtype=np.float32)
        for [i1,j1] in border:
            s1 = set()
            v1 = arr[i1][j1]
            for ni,nj in self.neighbours(i1,j1):
                if arr[ni][nj]==-1:
                    s1.add((ni,nj))
                if arr[ni][nj]==13:
                    v1-=1
            for (i,j) in s1:
                probability[i][j] += v1/len(s1)
        i,j = np.unravel_index(probability.argmax(),probability.shape)
        pyautogui.click(button='right',x=self.board_box[0]+(j+0.5)*self.tile_size[0],y=self.board_box[1]+(i+0.5)*self.tile_size[1])
        # line_length = self.cols * 3 + 1 
        # print("-"*line_length)
        # for i in range(self.rows):
        #     for j in range(self.cols):
        #         print("{:2}".format(probability[i][j]), end=" ") 
        #     print("\n")
        # print("-"*line_length)