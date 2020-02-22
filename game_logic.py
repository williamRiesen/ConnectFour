from settings import ROW_COUNT, COLUMN_COUNT


def create_board():
    board = [None] * ROW_COUNT
    for i in range(ROW_COUNT):
        board[i] = [0] * COLUMN_COUNT
    return board


def check_if_column_has_space(board, column):
    return board[ROW_COUNT - 1][column] == 0


def get_next_open_row(board, column, ROW_COUNT):
    for row in range(ROW_COUNT):
        if board[row][column] == 0:
            return row


def drop_checker(board, row, column, player):
    board[row][column] = player


def check_for_win(board, current_player):
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
