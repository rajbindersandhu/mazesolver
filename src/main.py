from window import Window, infoWindow
from maze import Maze

def main():
    data_lst = infoWindow()
    if data_lst:
        num_rows, num_cols, search_algo = data_lst
    else:
        return
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    maze = Maze(margin,margin,num_rows,num_cols,cell_size_x,cell_size_y,win)
    solving_maze = maze.solve(search_algo)
    win.wait_for_close()


main()