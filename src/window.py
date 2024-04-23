from tkinter import Tk, BOTH, Canvas, Button, Entry, Label, StringVar, ttk, Frame, XView, LEFT
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
        self.root_widget.destroy()
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)


def infoWindow():
    required_data =[]
    tk = Tk()
    tk.title("Maze Solver")

    #Lables
    frame1 = Frame(tk, width=800, height=600)
    frame1.pack(fill="x")
    row_label = Label(frame1, text="Number Of Rows: ", font=("Arial", 18))
    row_label.pack(side="left", padx=5,pady=5)
    row_input = Entry(frame1, font=("Arial", 18))
    row_input.pack(side="left", padx=5,pady=5)


    frame2 = Frame(tk, width=800, height=600)
    frame2.pack(fill="x")
    col_label = Label(frame2, text="Number Of Columns: ", font=("Arial", 18))
    col_label.pack(side="left", padx=5,pady=5)
    col_input = Entry(frame2, font=("Arial", 18))
    col_input.pack(padx=5,pady=5)

    # Dropdown menu for algorithm selection
    frame3 = Frame(tk, width=800, height=600)
    frame3.pack(fill="x")
    drop_label = Label(frame3, text="Select Search Algorithm", font=("Arial", 18))
    drop_label.pack(side="left")
    algorithm_var = StringVar(frame3)
    algorithm_var.set("DFS")  # Default selection

    algorithm_menu = ttk.Combobox(frame3, textvariable=algorithm_var, values=["DFS", "BFS"], font=("Arial", 18))
    algorithm_menu.pack(side="left", padx=5, pady=5)

    frame4 = Frame(tk, width=800, height=600)
    frame4.pack(fill="x")
    start_buttom = Button(frame4, text="Start" ,font=("Helvetica", 18),height=2,width=10,  command=lambda: return_data() if algorithm_menu.get() != "" else None, state="disabled")
    start_buttom.pack(padx=5, pady=5)

    def update_button(event):
        if check_input():
            start_buttom.config(state="normal")
        else:
            start_buttom.config(state="disabled")

    def check_input():
        rows = row_input.get()
        cols = col_input.get()
        algo = algorithm_var.get()
        if len(rows)>0 and len(cols)>0 and len(algo)>0:
            return True
        return False
    row_input.bind("<KeyRelease>", update_button)
    col_input.bind("<KeyRelease>", update_button)


    def return_data():
        required_data.append(int(row_input.get()))
        required_data.append(int(col_input.get()))
        required_data.append(algorithm_var.get())
        tk.destroy()

    tk.mainloop()
    return required_data

