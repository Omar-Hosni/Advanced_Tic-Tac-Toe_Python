from IPython.display import clear_output
import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))

    return position

def replay():

    choice = input('Play Again? Enter Yes or No ')
    return choice == 'Yes'

def player_input():
    marker = ''

    #ASK PLAYER 1 TO CHOOSE X OR O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    #ASSIGN PLAYER 2, THE OPPOSITE MARKER
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return(player1,player2)

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board,mark):
    #WIN TIC TAC TOE?

    #ALL ROWS
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or \
           (board[4] == mark and board[5] == mark and board[6] == mark)or\
           (board[1] == mark and board[2] == mark and board[3] == mark)or\
           (board[7] == mark and board[4] == mark and board[1] == mark)or\
           (board[8] == mark and board[5] == mark and board[2] == mark)or\
           (board[9] == mark and board[6] == mark and board[3] == mark)or\
           (board[7] == mark and board[5] == mark and board[6] == mark)or\
           (board[9] == mark and board[5] == mark and board[1] == mark))




def display_board(board):

    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


#WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe')

while True:
    #PLAY THE GAME

    ## SET EVERYTHING UP(BOARDS, WHOS FIRST, CHOOSE MARKERS X,O)
    test_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Ready to play? Y/N ')

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    #GAME PLAY
    while game_on:
        if turn == 'Player 1':
            # Show the board
            display_board(test_board)

            #Choose a position
            position = player_choice(test_board)
            #Placer the marker on the position
            place_marker(test_board,player1_marker,position)
            #Check if they won
            if win_check(test_board,player1_marker):
                display_board(test_board)
                print('Player 1 Has Won!!!')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'
            #Or check if there is a tie

            #No tie? and no win? Then next player's turn
        else:
            # Show the board
            display_board(test_board)

            # Choose a position
            position = player_choice(test_board)
            # Placer the marker on the position
            place_marker(test_board, player2_marker, position)
            # Check if they won
            if win_check(test_board, player2_marker):
                display_board(test_board)
                print('Player 2 Has Won!!!')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'
    ### PLAYER ONE TURN
    if not replay():
        break
