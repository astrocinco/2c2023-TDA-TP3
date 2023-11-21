# Abstract Data Types

class ProblemData:
    def __init__(self, A_set: set, B_subsets: dict):
        self.A_set = A_set
        self.B_subsets = B_subsets

    def __str__(self):

        return "All players: " + str(self.A_set) + "\nAll preferences: " + str(self.B_subsets)
