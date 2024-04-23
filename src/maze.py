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
        print("Building Maze...")
        self._break_walls_r(0,0)
        print("Maze is ready!!!")

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

    def _draw_cell(self):
        if self.window:
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    cell = self.cell_list[i][j]
                    cell.draw()
                    self._animate()
        else:
            return
    
    def _animate(self):
        if self.window is None:
            return
        self.window.redraw()
        # time.sleep(0.00005)

    def _break_entrance_and_exit(self):
        if self.cell_list:
            top_left_cell = self.cell_list[0][0]
            top_left_cell.has_top_wall = False
            self._draw_cell()
            bottom_right_cell = self.cell_list[self.num_rows-1][self.num_cols-1]
            bottom_right_cell.has_bottom_wall = False
            self._draw_cell()

    
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
                self._draw_cell()
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
