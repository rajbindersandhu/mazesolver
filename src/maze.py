from graphics import Cell, Point, Line
import time
import random
class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window=None,
            seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cell_list = []
        if seed:
            random.seed(seed)
        self._create_cell_list()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._draw_cell()
        self._reset_cell_visited()

    def _create_cell_list(self):
        top_left_x = self.x1
        top_left_y = self.y1
        bottom_right_x = top_left_x + self.cell_size_x
        bottom_right_y = top_left_y + self.cell_size_y
        for i in range(self.num_rows):
            self.cell_list.append([])
            for j in range(self.num_cols):
                top_left_point = Point(top_left_x, top_left_y)
                bottom_right_point = Point(bottom_right_x, bottom_right_y)
                self.cell_list[i].append(Cell(top_left_point, bottom_right_point, self.window))
                top_left_x = bottom_right_x
                bottom_right_x = top_left_x + self.cell_size_x
            top_left_x = self.x1
            bottom_right_x = top_left_x + self.cell_size_x
            top_left_y = bottom_right_y
            bottom_right_y = top_left_y + self.cell_size_y
        
        self._draw_cell()

    def _draw_single_cell(self, i,j):
        if self.window:
            cell = self.cell_list[i][j]
            cell.draw()
            self._animate(0.005)
        else: return

    def _draw_cell(self):
        if self.window:
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    cell = self.cell_list[i][j]
                    cell.draw()
                    self._animate(0.005)
        else:
            return
    
    def _animate(self, timeout):
        if self.window is None:
            return
        self.window.redraw()
        time.sleep(timeout)

    def _break_entrance_and_exit(self):
        if self.cell_list:
            top_left_cell = self.cell_list[0][0]
            top_left_cell.has_top_wall = False
            self._draw_single_cell(0,0)
            bottom_right_cell = self.cell_list[self.num_rows-1][self.num_cols-1]
            bottom_right_cell.has_bottom_wall = False
            self._draw_single_cell(self.num_rows-1, self.num_cols-1)

    
    def _break_walls_r(self, i,j):

        self.cell_list[i][j].visited = True
        while True:
            options = []
            if i == 0 and j == 0:
                if not self.cell_list[i][j+1].visited:
                    options.append((i, j + 1))
                if not self.cell_list[i+1][j].visited:
                    options.append((i + 1, j))
            elif i==len(self.cell_list) - 1 and j == len(self.cell_list[0]) - 1:
                if not self.cell_list[i-1][j].visited:
                    options.append((i-1,j))
                if not self.cell_list[i][j-1].visited:
                    options.append((i,j-1))
            elif (i == 0 and j == len(self.cell_list[0]) - 1):
                if not self.cell_list[i][j-1].visited:
                    options.append((i, j - 1))
                if not self.cell_list[i+1][j].visited:
                    options.append((i + 1, j))
            elif (i == len(self.cell_list) - 1 and j == 0):
                if not self.cell_list[i-1][j].visited:
                    options.append((i - 1, j))
                if not self.cell_list[i][j+1].visited:
                    options.append((i, j + 1))
            elif (i == 0):
                if not self.cell_list[i][j+1].visited:
                    options.append((i, j + 1))
                if not self.cell_list[i][j-1].visited:
                    options.append((i, j - 1))
                if not self.cell_list[i+1][j].visited:
                    options.append((i + 1, j))
            elif (j == 0):
                if not self.cell_list[i+1][j].visited:
                    options.append((i + 1, j))
                if not self.cell_list[i-1][j].visited:
                    options.append((i - 1, j))
                if not self.cell_list[i][j+1].visited:
                    options.append((i, j + 1))
            elif (j == len(self.cell_list[0]) - 1):
                if not self.cell_list[i+1][j].visited:
                    options.append((i + 1, j))
                if not self.cell_list[i-1][j].visited:
                    options.append((i - 1, j))
                if not self.cell_list[i][j-1].visited:
                    options.append((i, j - 1))
            elif (i == len(self.cell_list) - 1):
                if not self.cell_list[i][j+1].visited:
                    options.append((i, j + 1))
                if not self.cell_list[i][j-1].visited:
                    options.append((i, j - 1))
                if not self.cell_list[i-1][j].visited:
                    options.append((i - 1, j))
            else:
                if not self.cell_list[i+1][j].visited:
                    options.append((i + 1, j))
                if not self.cell_list[i-1][j].visited:
                    options.append((i - 1, j))
                if not self.cell_list[i][j+1].visited:
                    options.append((i, j + 1))
                if not self.cell_list[i][j-1].visited:
                    options.append((i, j - 1))
        
            if len(options) == 0:
                return
        
            selected_cell = random.choice(options)
            if selected_cell[0] == i-1 and selected_cell[1] == j:
                self.cell_list[i][j].has_top_wall = False
                self.cell_list[selected_cell[0]][selected_cell[1]].has_bottom_wall = False
            elif selected_cell[0] == i+1 and selected_cell[1] == j:
                self.cell_list[i][j].has_bottom_wall = False
                self.cell_list[selected_cell[0]][selected_cell[1]].has_top_wall = False
            elif selected_cell[0] == i and selected_cell[1] == j-1:
                self.cell_list[i][j].has_left_wall = False
                self.cell_list[selected_cell[0]][selected_cell[1]].has_right_wall = False
            elif selected_cell[0] == i and selected_cell[1] == j+1:
                self.cell_list[i][j].has_right_wall = False
                self.cell_list[selected_cell[0]][selected_cell[1]].has_left_wall = False
            self._break_walls_r(selected_cell[0], selected_cell[1])
    
    def _reset_cell_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                cell = self.cell_list[i][j]
                cell.visited = False

    def solve(self, search_algo = "DFS"):
        if search_algo == "DFS":
            return self._solve_dfs_r(0,0)
        elif search_algo == "BFS":
            return self._solve_bfs(0,0)
        else:
            raise Exception("Invalid search algorithm. Choose only from DFS or BFS")

    def _solve_dfs_r(self,i,j):
        self._animate(0.05)
        self.cell_list[i][j].visited = True
        if i==self.num_rows-1 and j==self.num_cols-1:
            return True

        for direction in [(i+1,j), (i-1,j), (i, j+1), (i,j-1)]:
            if(direction[0]>=0 and direction[0]<=self.num_rows-1 and direction[1]>=0 and direction[1]<=self.num_cols-1):
                if not self.cell_list[direction[0]][direction[1]].visited:
                    if direction[0] == i-1 and self.cell_list[i][j].has_top_wall:
                        continue
                    elif direction[0] == i+1 and self.cell_list[i][j].has_bottom_wall:
                        continue
                    elif direction[1] == j-1 and self.cell_list[i][j].has_left_wall:
                        continue
                    elif direction[1] == j+1 and self.cell_list[i][j].has_right_wall:
                        continue
                    else:
                        self.cell_list[i][j].draw_move(self.cell_list[direction[0]][direction[1]])
                        end_found = self._solve_dfs_r(direction[0], direction[1])
                        if end_found:
                            return True
                        self.cell_list[i][j].draw_move(self.cell_list[direction[0]][direction[1]], undo=True)
                else:
                    continue
            else:
                continue
        
        return False
    
    def _solve_bfs(self, i,j):
        to_visit=[]
        to_visit.append((i,j))
        while len(to_visit)>0:
            self._animate(0.05)
            current_cell = to_visit.pop()
            self.cell_list[current_cell[0]][current_cell[1]].visited = True
            if current_cell[0]==self.num_rows-1 and current_cell[1]==self.num_cols-1:
                return True
            
            for direction in [(current_cell[0]+1,current_cell[1]), (current_cell[0]-1,current_cell[1]), (current_cell[0], current_cell[1]+1), (current_cell[0],current_cell[1]-1)]:
                if(direction[0]>=0 and direction[0]<=self.num_rows-1 and direction[1]>=0 and direction[1]<=self.num_cols-1):
                    if not self.cell_list[direction[0]][direction[1]].visited:
                        if direction[0] == current_cell[0]-1 and self.cell_list[current_cell[0]][current_cell[1]].has_top_wall:
                            continue
                        elif direction[0] == current_cell[0]+1 and self.cell_list[current_cell[0]][current_cell[1]].has_bottom_wall:
                            continue
                        elif direction[1] == current_cell[1]-1 and self.cell_list[current_cell[0]][current_cell[1]].has_left_wall:
                            continue
                        elif direction[1] == current_cell[1]+1 and self.cell_list[current_cell[0]][current_cell[1]].has_right_wall:
                            continue
                        else:
                            to_visit=[direction] + to_visit
                            self.cell_list[current_cell[0]][current_cell[1]].draw_move(self.cell_list[direction[0]][direction[1]])
                            
                    else:
                        continue
                else:
                    continue
        return False
            