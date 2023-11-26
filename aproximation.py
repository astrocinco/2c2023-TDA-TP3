import pulp
import sys
sys.path.insert(1, '')

from datos.data_processing import map_txt


def map_file_and_aprox_by_lp(file_path):
    problem_data = map_txt(file_path)
    return aproximation_by_lineal_programming(problem_data)


def get_pulpvariable_by_name_in_list(variable_list, name):
    for variable in variable_list:
        if (variable.name == name):
            return variable


def aproximation_by_lineal_programming(problem_data):
    players_list = problem_data.players_as_list()
    problem_player_variables = list()
    for player in players_list:
        problem_player_variables.append(pulp.LpVariable(player, lowBound=0, upBound=1, cat='Continuous'))

    problem = pulp.LpProblem("players_selected", pulp.LpMinimize)

    biggest_subset = 0
    dict_in_problem_variables = dict()
    for journalist in problem_data.B_subsets:
        lista = problem_data.B_subsets[journalist]
        if (len(lista) > biggest_subset):
            print("Big subset:", len(lista))
            biggest_subset = len(lista)

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
    return list(map(lambda player: (player.name, pulp.value(player)), problem_player_variables)), biggest_subset


if __name__ == "__main__":
    aproximation_list, biggest_subset = map_file_and_aprox_by_lp("datos/sets_propios/400.txt")
    print("Biggest subset:", biggest_subset)
    
    # Valores para cada jugador, y cuantos son elegidos según 1/b
    aproximation_result = list(filter(lambda player: player[1] >= (1/biggest_subset), aproximation_list))
    print("Aproximation filtered >=", 1/biggest_subset, ":\n", aproximation_result)
    print("Difference:", len(aproximation_result), len(aproximation_list))

    # Esto es simplemente para mejorar la legibilidad, redondea los decimales
    rounded_list = list(map(lambda player: (player[0], round(player[1], 3)), aproximation_result))
    print("Rounded list:", rounded_list)