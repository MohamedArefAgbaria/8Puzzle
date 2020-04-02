this script solves the 8 puzzle problem .
to solve the problem I used A* algorithm based on manhattan heuristic.
this script shows to you the necessary steps to solve the problem . 

you can insert your "problem" board manually where the problems are defined at the top of the script. 
the problem describe the initial state of the board.
also you can change the goal test : the status that you want to achieve in the board.


for example:
initial state : [[4, 7, 8], [6, 3, 2], [' ', 5, 1]]
in my script this is the goal_test = [[1, 2, 3], [8, ' ', 4], [7, 6, 5]]

4  7  8               1  2  3
6  3  2     ==>       8  -  4
-  5  1               7  6  5
