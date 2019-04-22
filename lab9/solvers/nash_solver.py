from typing import List

from lab9.solvers.base_solver import BaseSolver


class NashSolver(BaseSolver):
    def _is_optimum_for_A(self, i: int, j: int) -> bool:
        A_column = self._get_column_for_A(j)
        return max(A_column) == self.matrix.row(i)[j][0]

    def _is_optimum_for_B(self, i: int, j: int) -> bool:
        B_row = self._get_row_for_B(i)
        return max(B_row) == self.matrix.row(i)[j][1]

    def _get_column_for_A(self, j: int) -> List[int]:
        return [x[0][0] for x in self.matrix.col(j).tolist()]

    def _get_row_for_B(self, i: int) ->  List[int]:
        return [x[1] for x in self.matrix.row(i).tolist()[0]]
