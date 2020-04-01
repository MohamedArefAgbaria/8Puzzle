"""
I answer the questions
(1) SOLUTION DEPTH
(2) EXPANDED NODES
(3) SOLUTION PATH
in this Script
problem1 is question(1)a
problem2 is question(1)b
problem3 is question(1)c
"""
import copy
problem1 = [[4, 7, 8], [6, 3, 2], [' ', 5, 1]]
problem2 = [[1, 4, 7], [2, 5, 8], [3, 6, ' ']]
problem3 = [[8, 3, 5], [1, ' ', 2], [6, 7, 4]]
goal_test = [[1, 2, 3], [8, ' ', 4], [7, 6, 5]]
correct_number_indexes1 = [(0, 0), (0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)]
left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)
frontier = []
closed = []
helper_closed = []
FAIL = -1
MAX_FRONTIER_LENGTH = 9*8*7*6*5*4*3*2


def user_interface():
    user_choice = input("CHOSE PROBLEM YOU WANT TO SOLVE:   (1)   (2)   (3)\n")
    if user_choice == "1":
        return problem1
    if user_choice == "2":
        return problem2
    if user_choice == "3":
        return problem3


def a_star(problem):
    frontier.append((problem, 0, calculate_heuristic(problem), calculate_heuristic(problem)))

    while len(frontier):
        min_value = get_min_f()
        frontier.remove(min_value)
        if min_value not in closed:
            helper_closed.append(min_value[0])
            closed.append(min_value)

        if min_value[0] == goal_test:
            print("PROBLEM SOLVED")
            return min_value[1]

        g_value = min_value[1]
        copy_min_value = copy.deepcopy(min_value)
        current_sate = copy.deepcopy(copy_min_value[0])
        actions = get_actions(current_sate)

        for action in actions:
            copy_current_state = copy.deepcopy(current_sate)
            successor(copy_current_state, action)
            if copy_current_state not in helper_closed:
                current_heuristic = calculate_heuristic(copy_current_state)
                frontier.append((copy_current_state, g_value+1, current_heuristic, current_heuristic+g_value+1))

            if len(helper_closed) == MAX_FRONTIER_LENGTH:
                print("Problem Not Solved")
                return FAIL
    return FAIL


def get_min_f():
    min_f_value = frontier[0][3]
    min_value = frontier[0]
    for problem in frontier:
        if problem[3] < min_f_value:
            min_value = problem
    return min_value


def print_board(board, i):
    print("               //////->Step {}<-////////".format(i))
    print("               *************************")
    for row in board:
            print_row(row)
    return board


def print_row(row):
    print("               *       *       *       *")
    print("               *   ", end='')
    print(row[0], end='')
    print("   *", end='')
    print("   ", end='')
    print(row[1], end='')
    print("   *", end='')
    print("   ", end='')
    print(row[2], end='')
    print("   *")
    print("               *       *       *       *")
    print("               *************************")


def get_actions(state):
    """format [ ( (position in the board),(direction) )] """
    empty_place = find_empty_place(state)
    option1 = empty_place[0]+up[0], empty_place[1]+up[1]
    option2 = empty_place[0]+down[0], empty_place[1]+down[1]
    option3 = empty_place[0]+left[0], empty_place[1]+left[1]
    option4 = empty_place[0] + right[0], empty_place[1]+right[1]
    optional_actions = [option1, option2, option3, option4]
    return check_legal_actions(optional_actions)


def find_empty_place(board):
    for row in range(3):
        for column in range(3):
            if board[row][column] == ' ':
                return row, column


def check_legal_actions(actions):
    all_positions = correct_number_indexes1+[(1, 1)]
    legal_actions = []
    if actions[0] in all_positions:
        legal_actions.append((actions[0], down))
    if actions[1] in all_positions:
        legal_actions.append((actions[1], up))
    if actions[2] in all_positions:
        legal_actions.append((actions[2], right))
    if actions[3] in all_positions:
        legal_actions.append((actions[3], left))
    return legal_actions


def successor(state, action):
    save_number = state[action[0][0]][action[0][1]]
    state[action[0][0]][action[0][1]] = ' '
    state[action[0][0] + action[1][0]][action[0][1] + action[1][1]] = save_number


def calculate_heuristic(state):
    total = 0
    for row in range(3):
        for column in range(3):
            place = (row, column)
            total += calculate_one_square_heuristic(place, state[row][column])
    return total


def calculate_one_square_heuristic(place, number):
    if number == ' ':
        return 0
    correct_place = correct_number_indexes1[number]
    return abs(correct_place[0]-place[0]) + abs(correct_place[1]-place[1])


def find_solution_path(closed_list, depth):
    solution_path = []
    current_state = closed_list[-1]
    solution_path.append(current_state)
    while len(solution_path) != (depth+1):
        for state in closed_list:
            if is_successor_in_solution_path(state, solution_path[-1]):
                closed_list.remove(state)
                solution_path.append(state)
    return solution_path


def is_successor_in_solution_path(state1, state2):
    count_differences = 0
    for i in range(3):
        for j in range(3):
            if state1[0][i][j] != state2[0][i][j]:
                count_differences += 1
    if count_differences == 2:
        if (state2[1] - state1[1]) == 1 and ((state1[2]-state2[2]) <= 2):
            return True
    return False


def print_path(solution_path):
    print("DO THESE STEPS TO SOLVE THE PROBLEM")
    for step in range(len(solution_path)):
        print_board(solution_path[len(solution_path) - step - 1][0], step)


if __name__ == "__main__":

    problem_to_solve = user_interface()
    solution_depth = a_star(problem_to_solve)
    if solution_depth != -1:
        print("SOLUTION OF PROBLEM IN DEPTH {0}".format(solution_depth))
        path = (find_solution_path(copy.deepcopy(closed), solution_depth))
        print_path(path)
        print("CLOSED LENGTH - ALGORITHEM EXTEND {} STATES (NODES)".format(len(closed)))
    else:
        print("PROBLEM NOT SOLVED HAVE NO SOLUTION!")

''' IF you choice the third problem you get the answer "PROBLEM NOT SOLVED HAVE NO SOLUTION " 
after a lot of time '''




