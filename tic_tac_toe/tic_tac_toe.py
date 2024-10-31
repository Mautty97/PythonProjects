'''
This program is a simple tic-tac-toe game for two players. Each player will take turns
selecting where to place their X or O. First to get 3 in a row, column or diagonal wins!

Author: Mautty97

'''


import os
from IPython.display import clear_output

#display the current board
def display(board):
    #mac clear screen
    os.system('clear')

    #windows clear screen
    #os.system('cls')

    #jupyter clear screen
    #clear_output()
    
    print(' '+board[0]+' | '+board[1]+' | '+board[2]+' ')
    print('----------- ')
    print(' '+board[3]+' | '+board[4]+' | '+board[5]+' ')
    print('----------- ')
    print(' '+board[6]+' | '+board[7]+' | '+board[8]+' ')

#have players decide who is going first
def player_select():
    player = ''
    while player not in ['X','x','O','o']:
        player = input("Player 1: Would you like to play as X's or O's?  ")
        #if not valid
        if player not in ['X','x','O','o']:
            print('Please choose either X or O')
        elif player in ['X', 'x']:
            print('Player 1 will go first','\n')
            return 'Player 1'
        elif player in ['O','o']:
            print("Player 2 will go first",'\n')
            return 'Player 2'

#get position of letter
def get_pos(board, current_player, current_letter):
    is_empty = True
    pos = ''
    while is_empty:
        pos = input(f'{current_player} where do you want to put your {current_letter}? ')

        #check if position is blank
        if board[int(pos)-1] == ' ':
            return int(pos)-1
        else:
            print('There is already something there, try a different square')



#edit the board 
def edit_board(board, position, letter):
    board[position] = letter
    return board

#check for a tie
def check_tie(board):
    for pos in board:
        if pos == ' ':
            return False
    return True
            

#check if the player won this turn
def check_win(board, letter):
    if letter == board[0] == board[1] == board[2]: #row 1
        return True
    elif letter == board[3] == board[4] == board[5]: #row 2
        return True
    elif letter == board[6] == board[7] == board[8]: #row 3
        return True
    elif letter == board[0] == board[3] == board[6]: #col 1
        return True
    elif letter == board[1] == board[4] == board[7]: #col 2
        return True
    elif letter == board[2] == board[5] == board[8]: #col 3
        return True
    elif letter == board[0] == board[4] == board[8]: #diagonal \
        return True
    elif letter == board[6] == board[4] == board[2]: #diagonal /
        return True
    else:
        return False

#switch current player
def next_player(player):
    if player == 'Player 1':
        return 'Player 2'
    else:
        return 'Player 1'

#switch current letter
def next_letter(letter):
    if letter == 'X':
        return 'O'
    else:
        return 'X'

#ask whether the user wants to play again
def play_again():
    playon = ''

    while playon not in ['Y','y','N','n']:
        playon = input('Would you like to play again? (y/n): ')
        if playon not in ['Y','y','N','n']:
            print('Sorry, please choose y or n')
        elif playon in ['Y','y']:
            return True
        else:
            return False

#----------------------------------------------------------------------------

#Game Starts Here
playon = True
board_locations = ['1','2','3','4','5','6','7','8','9']
board = [' ']*9
current_player = 'Player 1'
current_letter = 'X'
position = ''
game_over = False
tie = False



while playon:
    #show the players the numbers for each position
    display(board_locations)
    print('\n')
    print('The layout of the board is shown above:', '\n')
    print('Players will select a number 1-9 to indicate where they would like to place their letter.', '\n')

    #select which player goes first
    current_player = player_select()

    #input('Press enter to continue...')

    while not game_over and not tie:
        
        position = get_pos(board, current_player, current_letter)
        board = edit_board(board, position, current_letter)
        display(board)
        if check_win(board, current_letter):
            print(f'Congrats {current_player}, you won!')
            break
        elif check_tie(board):
            print('Looks like there was a tie!')
            break
        current_player = next_player(current_player)
        current_letter = next_letter(current_letter)

    playon = play_again()
    if playon == True:
        board = [' ']*9
    else:
        print('Thanks for playing!')
