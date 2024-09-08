'''
Code written by https://github.com/damilohundaffodil for the final assignment
for the Python Essentials 1 (Aligned with PCEP-30-02). Sharing it so others can
learn plus give me ways to improve it.

This code lets the user (you), to play tic tac toe with the computer (which just
generates random numbers)

It uses all the 'components' learned in this course including: flow of control,
conditional statements, data structures and exception handeling.

Have fun :)
'''

from random import randrange

#The blank board with the numbers
blank = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]

#the actual board being played on. X and Os will be put in here
board = [
    ['','',''],
    ['','',''],
    ['','','']
]

#the lookup table for the number and board coordinates
lookup = {1:(0,0), 2:(0,1), 3:(0,2),
          4:(1,0), 5:(1,1), 6:(1,2),
          7:(2,0), 8:(2,1), 9:(2,2)}

#board display
def display_board(board):
    for i in range(3):
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|',end='')
        for j in range(3):            
            if board[i][j]!='':
                val = board[i][j]
            else:
                val = blank[i][j]
            print('   '+val + '   |',end= '')
        print('\n|       |       |       |')
    print('+-------+-------+-------+')    
        
xi = 'X'
oi = 'O'

print('BLANK BOARD')
display_board(board = board)
print('===============================')

def enter_move(board):
    while True:    
        try:     
            user_input = int(input('Enter your move: '))
            x, y = lookup[user_input]
            while (board[x][y]!=''):
                if(board[x][y]!=''):
                    user_input = int(input('That space is already taken. Try again: '))
                    x, y = lookup[user_input]
            board[x][y] = oi
            display_board(board = board)
            break
        except(ValueError):
            print("Input Needs to be an integer")
        except(KeyError):
            print('Input needs to be between 1 and 10')

def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                free_fields.append((i,j))
    
    return free_fields

def victory_for(board, sign):
    if board[0][0]==board[0][1]==board[0][2] == sign:
        return True
    elif board[1][0]==board[1][1]==board[1][2] == sign:
        return True
    elif board[2][0]==board[2][1]==board[2][2] == sign:
        return True
    elif board[0][0]==board[1][0]==board[2][0] == sign:
        return True
    elif board[0][1]==board[1][1]==board[2][1] == sign:
        return True
    elif board[0][2]==board[1][2]==board[2][2] == sign:
        return True
    elif board[0][0]==board[1][1]==board[2][2] == sign:
        return True
    elif board[2][0]==board[1][1]==board[0][2] == sign:
        return True
    else:
        return False


def draw_move(board):
    print('Computer\'s Move')
    comp = randrange(1,10)
    x, y = lookup[comp]
    while (board[x][y]!=''):
        if(board[x][y]!=''):
            comp = randrange(1,10)
            x, y = lookup[comp]
    board[x][y] = xi
    display_board(board = board)

def game():
    print('The computer goes first')
    board[1][1] = xi
    display_board(board = board)
    while (len(make_list_of_free_fields(board))>0):
        enter_move(board)
        if (victory_for(board, oi)==True):
            print('You win!')
            break
        draw_move(board)
        if (victory_for(board, xi)==True):
            print('The Computer Wins!')
            break
    else:
        print('It is a tie!')

game()
