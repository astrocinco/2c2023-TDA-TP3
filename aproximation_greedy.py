import sys
sys.path.insert(1, '')
from datos.adt import ProblemData
from datos.data_processing import map_txt


# Greedy non-optimal solution
def aproximation_by_greedy(problem_data : ProblemData):
    choosen_players = set()
    appearances_by_player = count_appearances_by_player(problem_data)
    ordered_list_by_appereance = ordered_list_by_apperance_from_dict(appearances_by_player)

    for journalist in problem_data.B_subsets:
        subset = problem_data.B_subsets[journalist]
        choosen_players.add(choose_most_appeared_player_in_subset(subset, ordered_list_by_appereance))
    return len(choosen_players), list(map(lambda tuple: tuple[0], choosen_players))


def count_appearances_by_player(problem_data : ProblemData):
    apparances_by_player = dict()
    for player in problem_data.A_set:
        apparances_by_player[player] = 0

    for journalist in problem_data.B_subsets:
        journalist_list = problem_data.B_subsets[journalist]
        for player in journalist_list:
            apparances_by_player[player] += 1
    
    return apparances_by_player


def ordered_list_by_apperance_from_dict(appareance_dict : dict):
    ordered_list = list()
    for player in appareance_dict:
        ordered_list.append( (player, appareance_dict[player]) )
    return sorted(ordered_list, key= lambda player: player[1], reverse=True)


def choose_most_appeared_player_in_subset(subset: list, most_appeared: list):
    subset = set(subset)
    for player in most_appeared:
        if player[0] in subset:
            return player
    raise KeyError("Player not found", subset, most_appeared)


if __name__ == "__main__":
    archivo = "datos/sets_catedra/50.txt"
    problem_data = map_txt(archivo)
    #print("Problem data:", problem_data)
    n, solution = aproximation_by_greedy(problem_data)
    print("Solution:", solution) 
    print(f"Choosen players vs total players: {n} de {len(problem_data.A_set)}")
