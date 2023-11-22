import pulp
import sys
sys.path.insert(1, '')

from datos.data_processing import map_txt
from datos.adt import ProblemData


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

    problem.solve()
    return list(map(lambda player: (player.name, pulp.value(player)), problem_player_variables))


if __name__ == "__main__":
    print("Solution:", map_file_and_solve_by_lp("datos/sets_catedra/5.txt")) 


#def map_variables_from_dict(subsets):



""" def ejemplo():
    x = pulp.LpVariable("x")
    y = pulp.LpVariable("y")
    problem = pulp.LpProblem("products", pulp.LpMaximize)
    problem += 3 * x - y <= 0
    problem += x + 2 * y <= 14
    problem += x - y <= 2
    problem += 5 * x + 3 * y
    problem.solve()
    return pulp.value(x), pulp.value(y)


if __name__ == "__main__":
    x, y = ejemplo()
    print(x, y) """
