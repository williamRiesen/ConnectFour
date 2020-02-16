import numpy


def create_board(rows, columns):
    return numpy.zeros((rows, columns))


def check_if_column_has_space(board, column, ROW_COUNT):
    return board[ROW_COUNT - 1][column] == 0


def get_next_open_row(board, column, ROW_COUNT):
    for row in range(ROW_COUNT):
        if board[row][column] == 0:
            return row


def check_for_win(board, COLUMN_COUNT, ROW_COUNT, current_player):
    for column in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if board[row][column] == current_player and \
                    board[row][column + 1] == current_player and \
                    board[row][column + 2] == current_player and \
                    board[row][column + 3] == current_player:
                return True
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if board[row][column] == current_player and \
                    board[row + 1][column] == current_player and \
                    board[row + 2][column] == current_player and \
                    board[row + 3][column] == current_player:
                return True
    for column in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if board[row][column] == current_player and \
                    board[row + 1][column + 1] == current_player and \
                    board[row + 2][column + 2] == current_player and \
                    board[row + 3][column + 3] == current_player:
                return True
    for column in range(COLUMN_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if board[row][column] == current_player and \
                    board[row - 1][column + 1] == current_player and \
                    board[row - 2][column + 2] == current_player and \
                    board[row - 3][column + 3] == current_player:
                return True


def drop_checker(board, row, column, player):
    board[row][column] = player
