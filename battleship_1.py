from time import sleep
from random import randint

player_1_ships = []
player_2_ships = []

player_1_shots = []
player_2_shots = []


def get_coor(): # takes input and returns 2 coordinates
    choosing = True
    while choosing:
        choice = input().upper()
        try:
            if len(choice) != 2:
                print("You need to provide 2 signs")
                continue
            if choice[0] in ["A", "B", "C", "D", "E"]:
                if int(choice[1]) in [1,2,3,4,5]:
                    coor1 = ord(choice[0]) - 65
                    coor2 = int(choice[1]) - 1
                    choosing = False
                else:
                    print("Invalid choice")
                    continue
            elif int(choice[0]) in [1,2,3,4,5]:
                if choice[1] in ["A", "B", "C", "D", "E"]:
                    coor1 = ord(choice[1]) - 65
                    coor2 = int(choice[0]) - 1
                    choosing = False
                else:
                    print("Invalid choice")
                    continue
            else:
                print("Invalid choice")
                continue
        except(IndexError):
            print("You need to provide 2 coordinates")
            continue
        except(ValueError):
            print("Invalid choice")
            continue

    return [coor1,coor2]

def get_coor_AI(player_ships, player_shots): # returns AI coordinates
    result = []
    for i in player_shots:
        if i in player_ships:
            if i[0] > 0 and [i[0]-1, i[1]] not in player_shots:
                result = [i[0]-1, i[1]]
            elif i[0] < 4 and [i[0]+1, i[1]] not in player_shots:
                result = [i[0]+1, i[1]]
            elif i[1] > 0 and [i[0], i[1]-1] not in player_shots:
                result = [i[0], i[1]-1]
            elif i[1] < 4 and [i[0], i[1]+1] not in player_shots:
                result = [i[0], i[1]+1]
    while result == []:
        random_coors = [randint(0,4), randint(0,4)]
        if random_coors not in player_shots:
            result = random_coors

    return result

def print_deploy_board(coordinates,mark = "X"):# takes in the list of coordinates used and marking sign and prints out the updated board
    board = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]
    for i in coordinates:
        board[i[0]][i[1]] = mark
    print("\n     1   2   3   4   5")
    print("     _   _   _   _   _")
    for index, item in enumerate(board):
        print(chr(index + 65) + "  | " + " | ".join(item) + " |")
    print("\n")

def print_shoot_board(shots_coordinates, ships_coordinates):# takes in lists of coordinates used and prints out the updated board
    board = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]
    for i in shots_coordinates:
        if i in ships_coordinates:
            board[i[0]][i[1]] = "H"
        elif i not in ships_coordinates:
            board[i[0]][i[1]] = "O"
    print("\n     1   2   3   4   5")
    print("     _   _   _   _   _")
    for index, item in enumerate(board):
        print(chr(index + 65) + "  | " + " | ".join(item) + " |")
    print("\n")

def placing(player_ships, size): # takes in start/end coordinates and returns list of all marked coordinates in a straight line
    deploying = 1
    while deploying:
        print(f"\nSize of the ship you are deploying:    {size} tiles")
        print("\nYou are now selecting the beggining tile: ")
        beggining_tile = get_coor()
        print("\nYou are now selecting the end tile.")
        end_tile = get_coor()

        first_coors_sorted = sorted([beggining_tile[0], end_tile[0]])
        second_coors_sorted = sorted([beggining_tile[1], end_tile[1]])

        validating_free_space = True

        for i in range(first_coors_sorted[0], first_coors_sorted[1] + 1):
            if not validating_free_space:
                break
            if [i, end_tile[1]] in player_ships:
                print("\nOne or more tiles already taken")
                validating_free_space = False
                break
        for i in range(second_coors_sorted[0], second_coors_sorted[1] + 1):
            if not validating_free_space:
                break
            if [beggining_tile[0], i] in player_ships:
                print("\nOne or more tiles already taken")
                validating_free_space = False
                break

        if not validating_free_space:
            continue
        elif len(range(first_coors_sorted[0], first_coors_sorted[1])) > size - 1 or len(range(second_coors_sorted[0], second_coors_sorted[1])) > size - 1:
            print("\nYour ship is too long")
            continue
        elif len(range(first_coors_sorted[0], first_coors_sorted[1])) < size - 1 and len(range(second_coors_sorted[0], second_coors_sorted[1])) < size - 1:
            print("\nYour ship is too short")
            continue
        elif len(range(first_coors_sorted[0], first_coors_sorted[1])) > 0 and len(range(second_coors_sorted[0], second_coors_sorted[1])) == 0:
            for i in range(first_coors_sorted[0], first_coors_sorted[1] + 1):
                player_ships.append([i, end_tile[1]])
            deploying = 0
        elif len(range(first_coors_sorted[0], first_coors_sorted[1])) == 0 and len(range(second_coors_sorted[0], second_coors_sorted[1])) > 0:
            for i in range(second_coors_sorted[0], second_coors_sorted[1] + 1):
                player_ships.append([beggining_tile[0], i])
            deploying = 0
        elif len(range(first_coors_sorted[0], first_coors_sorted[1])) != 0 and len(range(second_coors_sorted[0], second_coors_sorted[1])) != 0:
            print("\nYour ships cannot be placed diagonally")
            continue

def placing_AI(player_ships, size): # NOT WORKING
    # placed_ships = []

    # for i in placed_ships:
    #     while i[0]-1,i[1] not in placed_ships
    #     if i[0] > 0 and [i[0]-1, i[1]] not in placed_ships:
    #         placed_ships.append([i[0]-1, i[1]])
    #         player_ships.append([i[0]-1, i[1]])
    #     elif i[0] < 4 and [i[0]+1, i[1]] not in placed_ships:
    #         placed_ships.append([i[0]+1, i[1]])
    #         player_ships.append([i[0]+1, i[1]])
    #     elif i[1] > 0 and [i[0], i[1]-1] not in placed_ships:
    #         placed_ships.append([i[0], i[1]-1])
    #         player_ships.append([i[0], i[1]-1])
    #     elif i[1] < 4 and [i[0], i[1]+1] not in placed_ships:
    #         placed_ships.append([i[0], i[1]+1])
    #         player_ships.append([i[0], i[1]+1])
    # while result == []:
    #     random_coors = [randint(0,4), randint(0,4)]
    #     if random_coors not in player_shots:
    #         result = random_coors
    pass
    

def placing_all(player_ships, mark):# uses placing() to place all 3 ships on the board for a given player
    print_deploy_board(player_ships, mark)
    placing(player_ships, 2)
    print("\n"*30)
    print_deploy_board(player_ships, mark)
    placing(player_ships, 2)
    print("\n"*30)
    print_deploy_board(player_ships, mark)
    placing(player_ships, 3)
    print("\n"*30)
    print_deploy_board(player_ships, mark)

def shooting(player_shots, player_ships): # takes in list of shots and ships coordinates and appends the shots while checking ships for duplicates
    shot = get_coor()
    if shot in player_shots:
        print("You have already shot at this tile")
    else:
        player_shots.append(shot)
    print("\n"*30)
    print_shoot_board(player_shots, player_ships)

def shooting_AI(player_shots, player_ships): # takes in list of shots and ships coordinates and appends the shots
    shot = get_coor_AI(player_ships, player_shots)
    player_shots.append(shot)
    print_shoot_board(player_shots, player_ships)

def win_loose(player_shots, player_ships): # takes in shots and ships coordinates and evaluates if they match
    for i in player_ships:
        if i not in player_shots:
            return False
    return True

def main(): # podzielic
    print("\nDeployment phase:")

    print("\nPlayer 1 starts")
    placing_all(player_1_ships, "X")
    sleep(3)
    print("\n"*30)

    print("\nComputer's turn ( please help him deploy :> )")
    placing_all(player_2_ships, "X")
    sleep(3)

    print("Shooting phase")
    while True:
        print("\n"*30)
        print("\nPlayer 1 shoots")
        print_shoot_board(player_1_shots, player_2_ships)
        shooting(player_1_shots, player_2_ships)
        sleep(3)
        if win_loose(player_1_shots, player_2_ships):
            print_shoot_board(player_1_shots, player_2_ships)
            print("\nPlayer 1 wins!")
            break
        print("\n"*30)
        print("\nComputer shoots")
        shooting_AI(player_2_shots, player_1_ships)
        sleep(3)
        if win_loose(player_2_shots, player_1_ships):
            print_shoot_board(player_2_shots, player_1_ships)
            print("\nComputer wins!")
            break

main()