import pulp
import sys
sys.path.insert(1, '')

from datos.data_processing import map_txt


def map_file_and_solve_by_lp(file_path):
    problem_data = map_txt(file_path)
    return solution_by_lineal_programming(problem_data)


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
    solution = map_file_and_solve_by_lp("datos/sets_catedra/200.txt")
    #solution = map_file_and_solve_by_lp("datos/sets_grandes/3005.txt")
    print("Solution:", solution) 
    solution_filtered = list(filter(lambda player: player[1] == 1, solution))
    print("Filtered solution", solution_filtered)
    print("Choosen players vs total players:", len(solution_filtered), len(solution))
