print(" WELCOME TO TIC TAC TOE GAME! ")
board = [ " - ", " - ", " - ",
          " - ", " - ", " - ",
          " - ", " - ", " - "]

def displayBoard():
    print("-------------")
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("-------------")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("-------------")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("-------------")

displayBoard()


gamekeepgoing = True
currentplayer = " X "
alreadytaken = False
while gamekeepgoing == True:
    # Ask the player to introduce a position in the board
    playerposition = int(input("Enter a position between 0 - 8: "))
    
    # Stop the game if the position is not in board
    if playerposition > 8 or playerposition < 0:
        print("The position does not exist. Try again. \n"
              "Choose a position between 0 and 8!!!")
        break


    # If the position chosen is already taken, tell the player to introduce another position
    if board[playerposition] != " - ":
        alreadytaken = True
        print("Already taken!")
        pass

    # If the position chosen is not taken, substitue the " - " on the board for the figure (X) or (O)
    else:
        board[playerposition] = currentplayer
        displayBoard()

        # If the current player is X, change the next player to O and vice versa
        if currentplayer == " X ":
            currentplayer = " O "
        elif currentplayer == " O ":
            currentplayer = " X "


    # Define the rules in case there is a winner
    if board[0] == board[1] == board[2] != " - ":
        winner = board[0]
        print(f"{winner} won!")
        gamekeepgoing = False
    elif board[3] == board[4] == board[5] != " - ":
        winner = board[3]
        print(f"{winner} won!")
        gamekeepgoing = False
    elif board[6] == board[7] == board[8] != " - ":
        winner = board[6]
        print(f"{winner} won!")
        gamekeepgoing = False
    elif board[0] == board[3] == board[6] != " - ":
        winner = board[0]
        print(f"{winner} won!")
        gamekeepgoing = False
    elif board[1] == board[4] == board[7] !=  " - ":
        winner = board[1]
        print(f"{winner} won!")
        gamekeepgoing = False
    elif board[2] == board[5] == board[8] != " - ":
        winner = board[2]
        print(f"{winner} won!")
        gamekeepgoing = False
    elif board[0] == board[4] == board[8] != " - ":
        winner = board[0]
        print(f"{winner} won!")
        gamekeepgoing = False
    elif board[2] == board[4] == board[6] != " - ":
        winner = board[2]
        print(f"{winner} won!")
        gamekeepgoing = False


    # Define what happens when there is no winner and all positions are taken
    result = board.count(" - ")
    if result == 0 and gamekeepgoing == True:
        print("It is a tie!")
        break
