import unittest
from maze import Maze

class MazeTest(unittest.TestCase):
    def test_creat_cell_list(self):
        num_rows = 5
        num_cols = 10
        maze = Maze(0,0,num_rows, num_cols,1,1)

        self.assertEqual(len(maze.cell_list), num_rows)
        self.assertEqual(len(maze.cell_list[0]), num_cols)

    def test_break_entry_and_exit(self):
        num_rows = 5
        num_cols = 10
        maze = Maze(0,0,num_rows, num_cols,1,1)

        maze._break_entrance_and_exit()

        self.assertFalse(maze.cell_list[0][0].has_top_wall)
        self.assertFalse(maze.cell_list[num_rows-1][num_cols-1].has_bottom_wall)

if __name__ == "__main__":
    unittest.main()