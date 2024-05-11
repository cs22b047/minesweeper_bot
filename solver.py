import pyautogui
class Solver:
 def __init__(self):
        self.rows=16
        self.cols=30
        self.board_box = (17,181,1730,1093)
        self.tile_size = ((self.board_box[2]-self.board_box[0])/30,(self.board_box[3]-self.board_box[1])/16)
        
    
 def dfs(self,arr,i,j,visited,border):
    flag = False
    if(i+1<self.rows):
        if(arr[i+1][j]==0):
            flag = True
    if(i-1>=0):
        if(arr[i-1][j]==0):
            flag = True
    if(j+1<self.cols):
        if(arr[i][j+1]==0):
            flag = True
    if(j-1>=0):
        if(arr[i][j-1]==0):
            flag = True
    if(i+1<self.rows and j+1<self.cols):
        if(arr[i+1][j+1]==0):
            flag = True
    if(i+1<self.rows and j-1>=0):
        if(arr[i+1][j-1]==0):
            flag = True
    if(i-1>=0 and j+1<self.cols):
        if(arr[i-1][j+1]==0):
            flag = True                 
    if(i-1>=0 and j-1>=0):
        if(arr[i-1][j-1]==0):
            flag = True
    if(flag):
        border.append([i,j])
    visited[i][j] = True
    if(i+1<self.rows):
        if(visited[i+1][j]==False and arr[i+1][j]>0 and arr[i+1][j]<=8):
            self.dfs(arr,i+1,j,visited,border)
    if(i-1>=0):
        if(visited[i-1][j]==False and arr[i-1][j]>0 and arr[i-1][j]<=8):
            self.dfs(arr,i-1,j,visited,border)
    if(j+1<self.cols):
        if(visited[i][j+1]==False and arr[i][j+1]>0 and arr[i][j+1]<=8):
            self.dfs(arr,i,j+1,visited,border)
    if(j-1>=0):
        if(visited[i][j-1]==False and arr[i][j-1]>0 and arr[i][j-1]<=8):
            self.dfs(arr,i,j-1,visited,border)
    if(i+1<self.rows and j+1<self.cols):
        if(visited[i+1][j+1]==False and arr[i+1][j+1]>0 and arr[i+1][j+1]<=8):
            self.dfs(arr,i+1,j+1,visited,border)
    if(i+1<self.rows and j-1>=0):
        if(visited[i+1][j-1]==False and arr[i+1][j-1]>0 and arr[i+1][j-1]<=8):
            self.dfs(arr,i+1,j-1,visited,border)                        
    if(i-1>=0 and j+1<self.cols):
        if(visited[i-1][j+1]==False and arr[i-1][j+1]>0 and arr[i-1][j+1]<=8):
            self.dfs(arr,i-1,j+1,visited,border)                       
    if(i-1>=0 and j-1>=0):
        if(visited[i-1][j-1]==False and arr[i-1][j-1]>0 and arr[i-1][j-1]<=8):
            self.dfs(arr,i-1,j-1,visited,border)

 def findMines(self,arr,seed):
    border = []
    visited = [[False]*self.cols for _ in range(self.rows)]
    self.dfs(arr,seed[0],seed[1],visited,border)
    for [i,j] in border:
            if(arr[i][j]>=1 and arr[i][j]<=8):
                num = arr[i][j]
                clicks = []
                if(i+1<self.rows):
                    if(arr[i+1][j]==0):
                        clicks.append([i+1,j])
                    if(arr[i+1][j]==13):
                        num-=1
                if(i-1>=0):
                    if(arr[i-1][j]==0):
                        clicks.append([i-1,j])
                    if(arr[i-1][j]==13):
                        num-=1
                if(j+1<self.cols):
                    if(arr[i][j+1]==0):
                        clicks.append([i,j+1])
                    if(arr[i][j+1]==13):
                        num-=1
                if(j-1>=0):
                    if(arr[i][j-1]==0):
                        clicks.append([i,j-1])
                    if(arr[i][j-1]==13):
                        num-=1
                if(i+1<self.rows and j+1<self.cols):
                    if(arr[i+1][j+1]==0):
                        clicks.append([i+1,j+1])
                    if(arr[i+1][j+1]==13):
                        num-=1
                if(i+1<self.rows and j-1>=0):
                    if(arr[i+1][j-1]==0):
                        clicks.append([i+1,j-1])
                    if(arr[i+1][j-1]==13):
                        num-=1
                if(i-1>=0 and j+1<self.cols):
                    if(arr[i-1][j+1]==0):
                        clicks.append([i-1,j+1])
                    if(arr[i-1][j+1]==13):
                        num-=1
                if(i-1>=0 and j-1>=0):
                    if(arr[i-1][j-1]==0):
                        clicks.append([i-1,j-1])
                    if(arr[i-1][j-1]==13):
                        num-=1
                if(len(clicks)==num):
                    for k in range(len(clicks)):
                        arr[clicks[k][0]][clicks[k][1]] = 13
                        pyautogui.click(button='right',x=self.board_box[0]+clicks[k][1]*self.tile_size[0]+25,y=self.board_box[1]+clicks[k][0]*self.tile_size[1]+25)
                        
    right_clicks = []
    left_clicks = []
    for [i1,j1] in border:
        for [i2,j2] in border:
                if i1-i2==1 or i1-i2==-1 or j1-j2==1 or j1-j2==-1:
                    s1 = set()
                    s2 = set()
                    v1 = arr[i1][j1]
                    v2 = arr[i2][j2]
                    if(i1+1<self.rows):
                        if(arr[i1+1][j1]==0):
                            s1.add((i1+1,j1))
                        if(arr[i1+1][j1]==13):
                            v1-=1
                    if(i1-1>=0):
                        if(arr[i1-1][j1]==0):
                            s1.add((i1-1,j1))
                        if(arr[i1-1][j1]==13):
                            v1-=1
                    if(j1+1<self.cols):
                        if(arr[i1][j1+1]==0):
                            s1.add((i1,j1+1))
                        if(arr[i1][j1+1]==13):
                            v1-=1
                    if(j1-1>=0):
                        if(arr[i1][j1-1]==0):
                            s1.add((i1,j1-1))
                        if(arr[i1][j1-1]==13):
                            v1-=1
                    if(i1+1<self.rows and j1+1<self.cols):
                        if(arr[i1+1][j1+1]==0):
                            s1.add((i1+1,j1+1))
                        if(arr[i1+1][j1+1]==13):
                            v1-=1
                    if(i1+1<self.rows and j1-1>=0):
                        if(arr[i1+1][j1-1]==0):
                            s1.add((i1+1,j1-1))
                        if(arr[i1+1][j1-1]==13):
                            v1-=1
                    if(i1-1>=0 and j1+1<self.cols):
                        if(arr[i1-1][j1+1]==0):
                            s1.add((i1-1,j1+1))
                        if(arr[i1-1][j1+1]==13):
                            v1-=1
                    if(i1-1>=0 and j1-1>=0):
                        if(arr[i1-1][j1-1]==0):
                            s1.add((i1-1,j1-1))
                        if(arr[i1-1][j1-1]==13):
                            v1-=1


                    if(i2+1<self.rows):
                        if(arr[i2+1][j2]==0):
                            s2.add((i2+1,j2))
                        if(arr[i2+1][j2]==13):
                            v2-=1
                    if(i2-1>=0):
                        if(arr[i2-1][j2]==0):
                            s2.add((i2-1,j2))
                        if(arr[i2-1][j2]==13):
                            v2-=1
                    if(j2+1<self.cols):
                        if(arr[i2][j2+1]==0):
                            s2.add((i2,j2+1))
                        if(arr[i2][j2+1]==13):
                            v2-=1
                    if(j2-1>=0):
                        if(arr[i2][j2-1]==0):
                            s2.add((i2,j2-1))
                        if(arr[i2][j2-1]==13):
                            v2-=1
                    if(i2+1<self.rows and j2+1<self.cols):
                        if(arr[i2+1][j2+1]==0):
                            s2.add((i2+1,j2+1))
                        if(arr[i2+1][j2+1]==13):
                            v2-=1
                    if(i2+1<self.rows and j2-1>=0):
                        if(arr[i2+1][j2-1]==0):
                            s2.add((i2+1,j2-1))
                        if(arr[i2+1][j2-1]==13):
                            v2-=1
                    if(i2-1>=0 and j2+1<self.cols):
                        if(arr[i2-1][j2+1]==0):
                            s2.add((i2-1,j2+1))
                        if(arr[i2-1][j2+1]==13):
                            v2-=1
                    if(i2-1>=0 and j2-1>=0):
                        if(arr[i2-1][j2-1]==0):
                            s2.add((i2-1,j2-1))
                        if(arr[i2-1][j2-1]==13):
                            v2-=1
                    if(len(s1&s2)!=0):
                     if(v1-v2 == len(s1.difference(s2))):
                        for tile in s1.difference(s2):
                            arr[tile[0]][tile[1]] = 13
                            right_clicks.append(tile)
                        for tile in s2.difference(s1):
                            left_clicks.append(tile)
    for tile in right_clicks:
        pyautogui.click(button='right',x=self.board_box[0]+tile[1]*self.tile_size[0]+25,y=self.board_box[1]+tile[0]*self.tile_size[1]+25)
        
    for tile in left_clicks:
        # el = driver.find_element(By.ID,"cell_"+str(tile[1])+"_"+str(tile[0]))
        # el.click()
        pyautogui.click(x=self.board_box[0]+tile[1]*self.tile_size[0]+25,y=self.board_box[1]+tile[0]*self.tile_size[1]+25)
    for [i,j] in border:
        pyautogui.click(x=self.board_box[0]+j*self.tile_size[0]+25,y=self.board_box[1]+i*self.tile_size[1]+25)
        
        