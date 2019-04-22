from typing import List, Tuple

from lab9.solvers.base_solver import BaseSolver


class ParetoSolver(BaseSolver):
    def _is_optimum_for_A(self, i: int, j: int) -> bool:
        column = [elem for x in self.matrix.tolist() for elem in x]
        current_value_A = self.matrix.row(i)[j][0]
        current_value_B = self.matrix.row(i)[j][1]

        estimations = []
        for temp_A, temp_B in column:
            if temp_A > current_value_A and temp_B >= current_value_B:
                estimations += [True]
            else:
                estimations += [False]
        return not any(estimations)

    def _is_optimum_for_B(self, i: int, j: int) -> bool:
        row = [elem for x in self.matrix.tolist() for elem in x]
        current_value_A = self.matrix.row(i)[j][0]
        current_value_B = self.matrix.row(i)[j][1]

        estimations = []
        for temp_A, temp_B in row:
            if temp_A >= current_value_A and temp_B > current_value_B:
                estimations += [True]
            else:
                estimations += [False]
        return not any(estimations)

    def _get_column_for_A(self, j: int) -> List[Tuple[int, int]]:
        return [x[0] for x in self.matrix.col(j).tolist()]

    def _get_row_for_B(self, i: int) -> List[Tuple[int, int]]:
        return self.matrix.row(i).tolist()[0]
