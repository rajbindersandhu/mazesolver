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
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
        if self.cell_list:
            top_left_cell = self.cell_list[0][0]
            top_left_cell.has_top_wall = False
            self._draw_cell()
            bottom_right_cell = self.cell_list[self.num_rows-1][self.num_cols-1]
            bottom_right_cell.has_bottom_wall = False
            self._draw_cell()
        
