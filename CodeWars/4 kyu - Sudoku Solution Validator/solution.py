def validSolution(board):  # board[i][j]
    # lines validation
    if not sudoku_line_validation(board):
        return False

    # Grid validation
    if not sudoku_grid_validation(board):
        return False
    return True


def sudoku_line_validation(board) -> bool:
    # lines validation
    for i in range(9):
        # check line in horizontal,
        # i is as vertical index
        if len(board[i]) > len(set(board[i])):
            return False

        # create vertical line,
        vertical_line = []
        for j in range(9):
            # j is as vertical index
            # i is as horizontal index
            vertical_line.append(board[j][i])

        # check line in verctial
        if len(vertical_line) > len(set(vertical_line)):
            return False
    return True


def sudoku_grid_validation(board) -> bool:
    grids, left_grid, center_grid, right_grid = [], [], [], []

    for i in range(0, 9):
        # create 3 grids
        left_grid.append(board[i][0:3])
        center_grid.append(board[i][3:6])
        right_grid.append(board[i][6:9])

        # appends created grids and clearer it.
        if i == 2 or i == 5 or i == 8:
            _multiple_appends(grids, left_grid, center_grid, right_grid)
            left_grid, center_grid, right_grid = [], [], []

    # create list from each grid in grids. It should be 9 elements on list.
    compare = map(lambda x: sum(x, []), grids)
    for x in compare:
        if len(set(x)) < 9:
            return False
    return True


def _multiple_appends(listname, *element):
    listname.extend(element)