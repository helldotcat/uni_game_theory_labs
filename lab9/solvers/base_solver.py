from abc import abstractmethod
from typing import List, Tuple

from sympy import Matrix


class BaseSolver:
    def __init__(self, matrix: Matrix):
        self.matrix = matrix

    def get_optimums(self) -> List[Tuple[int, int]]:
        optimums = []
        for i in range(self.matrix.rows):
            for j in range(self.matrix.cols):
                if self._check_situation(i ,j):
                    optimums.append((i, j))
        return optimums

    def _check_situation(self, i: int, j: int) -> bool:
        return self._is_optimum_for_A(i, j) and self._is_optimum_for_B(i, j)

    @abstractmethod
    def _is_optimum_for_A(self, i: int, j: int) -> bool:
        pass

    @abstractmethod
    def _is_optimum_for_B(self, i: int, j: int) -> bool:
        pass
