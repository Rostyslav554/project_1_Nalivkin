from random import randrange

def display_board(board):
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    free = make_list_of_free_fields(board)
    move = -1
    while move not in range(1, 10) or ((move - 1) // 3, (move - 1) % 3) not in free:
        try:
            move = int(input("Введіть ваш хід (1-9): "))
        except ValueError:
            continue
    row, col = (move - 1) // 3, (move - 1) % 3
    board[row][col] = 'O'

def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free.append((row, col))
    return free

def victory_for(board, sign):
    for row in board:
        if all(cell == sign for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    free = make_list_of_free_fields(board)
    move = randrange(len(free))
    row, col = free[move]
    board[row][col] = 'X'

board = [[str(3 * row + col + 1) for col in range(3)] for row in range(3)]
board[1][1] = 'X'

while True:
    display_board(board)
    if victory_for(board, 'X'):
        print("Комп'ютер виграв!")
        break
    if not make_list_of_free_fields(board):
        print("Нічия!")
        break
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("Ви виграли!")
        break
    if not make_list_of_free_fields(board):
        display_board(board)
        print("Нічия!")
        break
    draw_move(board)
