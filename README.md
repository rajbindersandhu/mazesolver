# Maze Solver

## Introduction

Maze solver app, is an illustration for *"**depth first search**"* and *"**breadth first search**"*, by solving a maze.

Applcation displays a maze in form of an matrix. Then app develops a maze by breaking walls between starting cell to exit cell in matrix. The maze displayed is different every time application is started.
Finally the application finds a path between start and exit cell using DFS or BFS.

## Application guide

To start the application use *"main.sh* file. When the bash file is executed it displays a windows.

![Info window](./images/info_window_empty.PNG)

Application takes user input for,
- Number of rows for maze
- Number of columns for maze
- Search algorithm (BFS or DFS)

*Note: If Number of rows, number of columns and search algorithm boxes are empty, **Start** button will not work*

For search algorithm , one can only select out of DFS nad BFS

![Search Algorithm](./images/algo.PNG)

Once all values are entered and start button is clicked. A new window appears with a matrix having number of rows and coulumns added by user

![Maze matrix](./images/Maze_full.PNG)

The application develops maze using DFS by breaking walls fo the cell randomly to develop a random maze, evry time the application is started

![Maze structure](./images/Maze_hollow.PNG)

Now maze is ready, now the application , depending on the search algorithm selected, it starts searching a way out from start to exit.

![DFS search](./images//Maze_dfs.PNG)

![BFS search](./images/Maze_bfs.PNG)

