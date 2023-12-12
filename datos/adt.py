# Abstract Data Types
class ProblemData:
    def __init__(self, A_set: set, B_subsets: dict):
        self.A_set = A_set
        self.B_subsets = B_subsets

    def __str__(self):
        subsets_prints = ""
        for subset in self.B_subsets:
            subsets_prints += "    " + subset + str(self.B_subsets[subset]) + "\n"
        return "All players: " + str(self.A_set) + "\nAll preferences:\n" + subsets_prints
    
    def players_as_list(self):
        return list(self.A_set)
    