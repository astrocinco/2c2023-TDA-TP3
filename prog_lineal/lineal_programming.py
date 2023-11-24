import pulp
import sys
sys.path.insert(1, '')

from datos.adt import ProblemData
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

def prepocessing_subsets(journalists, problem_variables):
        
    subsets_with_variables = dict()
    for journalist in journalists:
        lista = journalists[journalist]
        mapped_list = []
        for player in lista:
            player_variable = get_pulpvariable_by_name_in_list(problem_variables, player)
            mapped_list.append(player_variable)
            subsets_with_variables[journalist] = mapped_list
    
    return subsets_with_variables

def formating_solution(problem_variables):
    solution = list(map(lambda player: (player.name, pulp.value(player)), problem_variables))
    return [player[0] for player in list(filter(lambda player: player[1] == 1, solution))]

def solution_by_lineal_programming(data : ProblemData):
    journalists = data.B_subsets
    players_list = data.players_as_list()

    problem_variables = [ pulp.LpVariable(player, cat="Binary") for player in players_list ]
    
    subsets_with_variables = prepocessing_subsets(journalists, problem_variables)
    
    problem = pulp.LpProblem("players_selected", pulp.LpMinimize)

    for journalist in subsets_with_variables:
        preferences_list = subsets_with_variables[journalist]
        problem += pulp.LpAffineExpression([(preferences_list[i], 1) for i in range(len(preferences_list))]) >= 1

    problem += pulp.LpAffineExpression([(problem_variables[i], 1) for i in range(len(problem_variables))])
    problem.solve()
    
    convocked = formating_solution(problem_variables)
    
    return len(convocked), convocked

if __name__ == "__main__":
    problem_data = map_txt("datos/sets_catedra/200.txt")
    n, players_convoked = solution_by_lineal_programming(problem_data)
    #solution = map_file_and_solve_by_lp("datos/sets_grandes/3005.txt")
    print("Solution:", players_convoked) 
    print(f"Choosen players vs total players: {n} de {len(problem_data.A_set)}")
    print(f"Verified solution: {check_solution(problem_data.B_subsets, players_convoked)}")
