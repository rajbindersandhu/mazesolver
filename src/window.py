from tkinter import Tk, BOTH, Canvas
from graphics import Line

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title("Maze Solver")
        self.canvas = Canvas(self.root_widget, bg="white", height=self.height, width=self.width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window is closed...")
    
    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

