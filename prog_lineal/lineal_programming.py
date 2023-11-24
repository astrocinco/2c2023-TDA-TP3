import pulp
import sys
sys.path.insert(1, '')

from datos.data_processing import map_txt

def check_solution(journalists : dict, players_convoked : list):   
    aux = set()
    for player in players_convoked:
        for journalist in journalists.keys():
            if player in journalists[journalist]:
                aux.add(journalist)
    
    return len(aux) == len(journalists.keys())


def get_pulpvariable_by_name_in_list(variable_list, name):
    for variable in variable_list:
        if (variable.name == name):
            return variable


def solution_by_lineal_programming(problem_data):
    players_list = problem_data.players_as_list()
    problem_player_variables = list()
    for player in players_list:
        problem_player_variables.append(pulp.LpVariable(player, cat="Binary"))

    problem = pulp.LpProblem("players_selected", pulp.LpMinimize)

    dict_in_problem_variables = dict()
    for journalist in problem_data.B_subsets:
        lista = problem_data.B_subsets[journalist]
        mapped_list = []
        for player in lista:
            player_variable = get_pulpvariable_by_name_in_list(problem_player_variables, player)
            mapped_list.append(player_variable)
        dict_in_problem_variables[journalist] = mapped_list

    for journalist in dict_in_problem_variables:
        preferences_list = dict_in_problem_variables[journalist]
        problem += pulp.LpAffineExpression([(preferences_list[i], 1) for i in range(len(preferences_list))]) >= 1

    problem += pulp.LpAffineExpression([(problem_player_variables[i], 1) for i in range(len(problem_player_variables))])
    problem.solve()
    return list(map(lambda player: (player.name, pulp.value(player)), problem_player_variables))

if __name__ == "__main__":
    problem_data = map_txt("datos/sets_catedra/200.txt")
    solution = solution_by_lineal_programming(problem_data)
    #solution = map_file_and_solve_by_lp("datos/sets_grandes/3005.txt")
    print("Solution:", solution) 
    solution_filtered = list(filter(lambda player: player[1] == 1, solution))
    players_convoked = [player[0] for player in solution_filtered]
    print("Filtered solution", players_convoked)
    print(f"Choosen players vs total players: {len(solution_filtered)} de {len(solution)}")
    print(f"Verified solution: {check_solution(problem_data.B_subsets, players_convoked)}")
