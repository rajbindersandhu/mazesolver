from tkinter import BOTH
class Point:
    def __init__(self, x=0,y=0):
        self.x= x
        self.y=y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        line = canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)

class Cell:
    def __init__(
            self, point_top_left, 
            point_bottom_right,
            window=None, 
            has_left_wall= True, 
            has_right_wall=True, 
            has_top_wall=True, 
            has_bottom_wall=True
            ):
        self.window = window
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.point_top_left = point_top_left
        self.point_bottom_right = point_bottom_right
        self.visited = False

    def draw(self, fill_color="black"):
        point_bottom_left = Point(self.point_top_left.x, self.point_bottom_right.y)
        point_top_right = Point(self.point_bottom_right.x, self.point_top_left.y)
        top_line = Line(self.point_top_left, point_top_right)
        bottom_line = Line(point_bottom_left, self.point_bottom_right)
        left_line = Line(self.point_top_left, point_bottom_left)
        right_line = Line(point_top_right, self.point_bottom_right)
        if self.has_top_wall:
            self.window.draw_line(top_line, fill_color)
        else:
            self.window.draw_line(top_line, "white")
        if self.has_bottom_wall:
            self.window.draw_line(bottom_line, fill_color)
        else:
            self.window.draw_line(bottom_line, "white")
        if self.has_left_wall:
            self.window.draw_line(left_line, fill_color)
        else:
            self.window.draw_line(left_line, "white")
        if self.has_right_wall:
            self.window.draw_line(right_line, fill_color)
        else:
            self.window.draw_line(right_line, "white")
    
    def draw_move(self, to_cell, undo=False):
        start_x = ((self.point_bottom_right.x - self.point_top_left.x)//2) +  self.point_top_left.x
        start_y = ((self.point_bottom_right.y - self.point_top_left.y)//2) +  self.point_top_left.y

        end_x = ((to_cell.point_bottom_right.x - to_cell.point_top_left.x)/2) +  to_cell.point_top_left.x
        end_y = ((to_cell.point_bottom_right.y - to_cell.point_top_left.y)/2) +  to_cell.point_top_left.y

        fill_color = "red"
        if undo:
            fill_color = "gray"

        start_point = Point(start_x, start_y)
        end_point = Point(end_x, end_y)
        mid_line = Line(start_point, end_point)

        self.window.draw_line(mid_line, fill_color)



        
    