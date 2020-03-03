import random


def displayBoard(board):
    """
    This function points out the board so that number pad can be used as a reference
    """
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def playerInput():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1: Choose X or O: ').upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def placeMarker(board, marker, position):
    board[position] = marker


def winCheck(board, mark):
    # WIN tic tac toe
    # all rows , and check to see if they all share the same marker?
    """
    across the top
    across the middle
    across the bottom
    down the middle
    down the middle
    down the right side
    diagonal
    diagonal
    """

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or (
            board[4] == mark and board[5] == mark and board[6] == mark) or (
        board[1] == mark and board[2] == mark and board[3] == mark) or (
        board[7] == mark and board[4] == mark and board[1] == mark) or (
        board[8] == mark and board[5] == mark and board[2] == mark) or (
        board[9] == mark and board[6] == mark and board[3] == mark) or (
        board[7] == mark and board[5] == mark and board[3] == mark) or (
        board[9] == mark and board[5] == mark and board[1] == mark))

    # all columns , check to see if marker matches
    # 2 diagonals , check to see match


def chooseFirst():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def spaceCheck(board, position):
    return board[position] == ' '


def fullBoardCheck(board):
    # function to check if any remaining blanks are in the board
    for i in range(1, 10):
        if spaceCheck(board, i):
            return False
    # board is full is we return true
    return True


def playerChoice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not spaceCheck(board, position):
        position = int(input('Choose a position: (1-9) '))
    return position


def replay():
    choice = input("Play again? Enter Yes or Not : ")
    return choice == 'Yes'


print('Welcome the tic toc toe')

while True:
    # play the game

    # set everything up(board,whose first,choose markers x,o)
    theBoard = [' '] * 10
    player1Marker, player2Marker = playerInput()

    turn = chooseFirst()
    print(turn + ' will go first')

    playGame = input('Ready to play? y or n? ')

    if (playGame == 'y'):
        gameOn = True
    else:
        gameOn = False

    # game play
    while gameOn:
        # player one turn
        if turn == 'Player 1':
            # show the board
            displayBoard(theBoard)
            # choose a position
            position = playerChoice(theBoard)
            # place the marker on the position
            placeMarker(theBoard, player1Marker, position)
            # check if they won
            if winCheck(theBoard, player1Marker):
                displayBoard(theBoard)
                print('Player 1 has won!')
                gameOn = False
            else:
                # Or check if they is a tie
                if fullBoardCheck(theBoard):
                    displayBoard(theBoard)
                    print('TIE GAME')
                    gameOn = False
                else:
                    #  no tie and no win? then next player turn
                    turn = 'Player 2'

        else:
            # player two turn
            # show the board
            displayBoard(theBoard)
            # choose a position
            position = playerChoice(theBoard)
            # place the marker on the position
            placeMarker(theBoard, player2Marker, position)
            # check if they won
            if winCheck(theBoard, player2Marker):
                displayBoard(theBoard)
                print('Player 2 has won!')
                gameOn = False
            else:
                # Or check if they is a tie
                if fullBoardCheck(theBoard):
                    displayBoard(theBoard)
                    print('TIE GAME')
                    gameOn = False
                else:
                    #  no tie and no win? then next player turn
                    turn = 'Player 1'

    if not replay():
        break
# break out of the while loop on replay
