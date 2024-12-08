from random import choice


def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |   {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |   {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |   {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


    def print_scoreboard(score_board):
        print("\t--------------------------------")
        print("\t              SCOREBOARD       ")
        print("\t--------------------------------")


        players = list(score_board.keys())
        print("\t   ", players[0], "\t   ", score_board[players[0]])
        print("\t   ", players[1], "\t   ", score_board[players[1]])

        print("\t--------------------------------\n")


    def single_game(cur_player):
        value = [' ' for x in range(9)]

        player_pos = {'X' : [], '0': []}


print_tic_tac_toe([' ' for x in range(9)])

while True:
    print_tic_tac_toe(values)

    try:
        print("Player", cur_player, " turn. Which box? : ", end="")
        move = int(input())
    except ValueError:
        print("Wrong Input! Try again")
        continue

        if move <1 or move >9:
            print("Wrong Input! Try again")
            continue

            if values[move - 1] != ' ':
                print("Place already filled. Try Again!!")
                continue

    values[move - 1]   = cur_player

    player_pos[cur_player].append(move)



    def check_win(player_pos, cur_player):

        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                [1, 4, 7], [2, 5, 8], [3, 6, 9],
                [1, 5, 9], [3, 5, 7]]

        for x in soln:
            if all(y in player_pos[cur_player] for y in x):
                return True

            return False

        def check_draw(player_pos):
            if len(player_pos['X']) + len(player_pos['O']) == 9:
                return True
            return False

        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, "has won the game!!")
            print("\n")
            return cur_player

        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Games Draw")
            print("\n")
            return 'D'

        if cur_player == 'X':
            cur_player == '0'
        else:
            cur_player = 'X'

    if __name__ == "__main__":
        print("Player 1")
        player1 = input("Enter the game : ")
        print("\n")

        print("Player 2")
        player1 = input("Enter the game : ")
        print("\n")

        cur_player = player1

        player_choice = {'X': "", '0': ""}
        options = ['X', '0']

        score_board = {player1: 0, player2: 0}
        print_scoreboard(score_board)

        while True:

            print("Turn to choose for", cur_player)
            print("Enter 1 for X")
            print("Enter 2 for 0")
            print("Enter 3 for Quit")

            try:
                choice = int(input())
            except ValueError:
                print ("Wrong Input!!! Try Again\n")
                continue

                if choice == 1:
                    player_choice['X'] = cur_player
                    if cur_player == player1:
                        player_choice['0'] = player2
                    else:
                        player_choice['0'] = player1
