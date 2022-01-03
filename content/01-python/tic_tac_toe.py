import sys

board = """
 {s1:^3} | {s2:^3} | {s3:^3}
-----+-----+-----
 {s4:^3} | {s5:^3} | {s6:^3}
-----+-----+-----      123
 {s7:^3} | {s8:^3} | {s9:^3}       456
                       789
"""


def initialize_board(play):
    for n in range(9):
        play["s{}".format(n+1)] = ""

def show_board(play):
    """ display the playing board.  We take a dictionary with the current state of the board
    We rely on the board string to be a global variable"""
    print(board.format(**play))


def get_move(n, xo, play):
    """ ask the current player, n, to make a move -- make sure the square was not
        already played.  xo is a string of the character (x or o) we will place in
        the desired square """
    valid_move = False
    while not valid_move:
        idx = input("player {}, enter your move (1-9): ".format(n))
        if play["s{}".format(idx)] == "":
            valid_move = True
        else:
            print("invalid: {}".format(play["s{}".format(idx)]))

    play["s{}".format(idx)] = xo


def check_win(play):

    # winning combinations
    combos = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
              (1, 4, 7), (2, 5, 8), (3, 6, 9),
              (1, 5, 9), (7, 5, 3)]

    winner = None

    for c in combos:
        # if we are empty, then pass
        if play["s{}".format(c[0])] == "":
            continue
        if play["s{}".format(c[0])] == play["s{}".format(c[1])] and \
           play["s{}".format(c[0])] == play["s{}".format(c[2])]:
            winner = play["s{}".format(c[0])]
            break

    return winner

def play_game():
    """ play a game of tic-tac-toe """

    # initialize the board
    play = {}
    initialize_board(play)

    symbols = ["x", "o"]

    for n in range(9):
        show_board(play)

        player = n % 2

        get_move(player, symbols[player], play)

        winner = check_win(play)
        if winner is not None:
            show_board(play)
            print("winner is {}!!!".format(winner))
            sys.exit()

if __name__ == "__main__":
    play_game()

