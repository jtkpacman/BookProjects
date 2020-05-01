# Tic Tac Toe game, created by Jacob Kenyon.

# Game variables.
# First create the board.
the_board = {"top_left": ' ', "top_mid": ' ', "top_right": ' ',
             "mid_left": ' ', "mid_mid": ' ', "mid_right": ' ',
             "bot_left": ' ', "bot_mid": ' ', "bot_right": ' '}

# I'm making a dictionary to store an integer value as a board marker.
# I believe this will make the movement easier for the user.
board_key = {1: "top_left", 2: "top_mid", 3: "top_right",
             4: "mid_left", 5: "mid_mid", 6: "mid_right",
             7: "bot_left", 8: "bot_mid", 9: "bot_right"}

current_player = 'X'
mark_position = 0
game_round = 0
game_won = False
mark_acceptable = False


# Print the board.
def printBoard(board):
    print(board["top_left"] + " | " + board["top_mid"] + " | " + board["top_right"] + "\n" +
          "- + - + -" + "\n" +
          board["mid_left"] + " | " + board["mid_mid"] + " | " + board["mid_right"] + "\n" +
          "- + - + -" + "\n" +
          board["bot_left"] + " | " + board["bot_mid"] + " | " + board["bot_right"])


# Mark the board.
def markBoard(board, space, player):
    new_board = board

    if board[board_key[int(space)]] == ' ':
        new_board[board_key[int(space)]] = player
        return new_board
    elif board[board_key[int(space)]] != ' ':
        print("There is already a mark there!")
        return board
    else:
        print("There has been some other error!")
        return board


# Check the board for a winning match.
def check_board(board):
    win = False

    if game_round < 10:
        # Horizontal Wins. #
        # Top row.
        if board["top_left"] == board["top_mid"] == board["top_right"] and board["top_left"] != ' ':
            winner = board["top_left"]
            print("The winner is " + winner + "!")
            printBoard(board)
            win = True

        # Middle row.
        if board["mid_left"] == board["mid_mid"] == board["mid_right"] and board["mid_left"] != ' ':
            winner = board["mid_left"]
            print("The winner is " + winner + "!")
            printBoard(board)
            win = True

        # Bottom row.
        if board["bot_left"] == board["bot_mid"] == board["bot_right"] and board["bot_left"] != ' ':
            winner = board["bot_left"]
            print("The winner is " + winner + "!")
            printBoard(board)
            win = True

        # Vertical Wins. #
        # Left column.
        if board["top_left"] == board["mid_left"] == board["bot_left"] and board["top_left"] != ' ':
            winner = board["top_left"]
            print("The winner is " + winner + "!")
            printBoard(board)
            win = True

        # Middle column.
        if board["top_mid"] == board["mid_mid"] == board["bot_mid"] and board["top_mid"] != ' ':
            winner = board["top_mid"]
            print("The winner is " + winner + "!")
            printBoard(board)
            win = True

        # Right column.
        if board["top_right"] == board["mid_right"] == board["bot_right"] and board["top_right"] != ' ':
            winner = board["top_right"]
            print("The winner is " + winner + "!")
            printBoard(board)
            win = True

        # Diagonal Wins. #
        # Bot left - Top Right.
        if board["bot_left"] == board["mid_mid"] == board["top_right"] and board["bot_left"] != ' ':
            winner = board["bot_left"]
            print("The winner is " + winner + "!")
            printBoard(board)
            win = True

        # Top right - Bot left.
        if board["top_left"] == board["mid_mid"] == board["bot_right"] and board["top_left"] != ' ':
            winner = board["top_left"]
            print("The winner is " + winner + "!")
            printBoard(board)
            win = True
    else:
        print("It's a tie! There is no winner!")
        printBoard(board)
        win = True
    return win


# Game Loop.
while not game_won:
    printBoard(the_board)
    print("Welcome to the Tic Tac Toe game, you are player " + current_player + ".\n" +
          "The top left space is marker 1 the top right is marker 3.\n" +
          "The bottom right marker is number 9... Where would you like to place\n" +
          "a marker at?..")

    while True:
        space = int(input())

        if the_board[board_key[space]] != ' ':
            print("Please pick another location.\n" +
                  "This one has been marked already.")
        elif the_board[board_key[space]] == ' ':
            markBoard(the_board, space, current_player)
            break
        else:
            print("There has been an issue.")

    # Iterate the round each time to keep track of the current round.
    game_round += 1

    # Check the board for a winner.
    # If the game is determined to be over it will return a True value for the game_won variable.
    game_won = check_board(the_board)

    # Change players at the end of each round.
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    else:
        current_player = 'X'
