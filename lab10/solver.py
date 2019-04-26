from lab10.tree import Tree


class Solver:
    def __init__(self, tree: Tree):
        self.tree = tree

    def solve(self):
        for i in reversed(range(self.tree.depth)):
            self.tree.make_reversed_induction_step(level=i)

    def print_results(self):
        pass
