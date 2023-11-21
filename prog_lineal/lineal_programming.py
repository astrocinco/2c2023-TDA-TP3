import pulp
import sys
sys.path.insert(1, '')

from datos.data_processing import map_txt
from datos.adt import ProblemData

def map_file_and_solve_by_lp(file_path):
    five_subsets_problem_data = map_txt("datos/sets_catedra/5.txt")
    print(five_subsets_problem_data)

def solution_by_lineal_programming():
    return


if __name__ == "__main__":
    map_file_and_solve_by_lp("x")


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
