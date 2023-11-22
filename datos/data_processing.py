import sys
sys.path.insert(1, '')
from datos.adt import ProblemData

def map_txt(file_path):
    all_players = set()
    all_preferences = dict()

    with open(file_path) as file:
        contador = 0
        for line in file:
            line = line.replace(" ", "")
            line = line.replace("'", "")
            player_list = line[:-1].split(",")
            all_preferences["journalist" + str(contador)] = player_list
            for player in player_list:
                if player not in all_players:
                    all_players.add(player)
            contador += 1

    return ProblemData(all_players, all_preferences)