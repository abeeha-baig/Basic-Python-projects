import itertools

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l [0] != 0:
            return True
        else:
            return False
    #horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f"player{row[0]} is the winner horizontally")
            return True

#vertical
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"player{check[0]} is the winner vertically")
            return True
        
#diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"player{diags[0]} is the winner diagonally")
        return True
    diags = []
    for ix in range (len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"player{diags[0]} is the winner diagonally")
        return True
    return False

def game_board(game_map, player=0, row=0, column=0, just_display= False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied! Try again!")
            return game_map, False
        print ("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
       print("error!: did you write the correct row/column index??", e)
       return game_map, False
    
    except Exception as e:
        print("something went wrong!!!", e)
        return game_map, False
play = True
players = [1, 2]

while play:
    game_size = int(input("what should be the size of the game? "))
    game = [[0 for i in range (game_size)] for i in range (game_size)]
    game_won = False
    game, _ = game_board(game, just_display = True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"current player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("what column do you want to play? (0, 1, 2): "))
            row_choice = int(input("what row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("do you want to play again? y/n  ")
            if again.lower() == "y":
                print("restarting...")
            elif again.lower() == "n":
                print("will wait for you to get back!")
            else:
                print("try again with y or n! :)")    
                play = False

win(game)