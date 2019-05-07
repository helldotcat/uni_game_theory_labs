from typing import Tuple

from sympy import Matrix

from lab12.print import print_matrix

class Solver:
    def __init__(self, trust_matrix: Matrix):
        self.trust_matrix = trust_matrix

    def get_final_opinions(self, opinions_vector: Matrix, epsilon_limit: float = 0.000001) -> Tuple[Matrix, int]:
        iterations = 0
        epsilon = 1
        iterated_matrix = self.trust_matrix
        final_opinions_vector = Matrix()

        while epsilon > epsilon_limit:
            iterations += 1
            iterated_matrix = iterated_matrix.multiply(self.trust_matrix)

            final_opinions_vector = iterated_matrix.multiply(opinions_vector.T)
            epsilon = self._calculate_epsilon(final_opinions_vector)

        print('Сошедшаяся матрица')
        print_matrix(iterated_matrix)
        print()

        return final_opinions_vector.T, iterations

    def _calculate_epsilon(self, matrix: Matrix) -> float:
        min_val = min(matrix.row(0).tolist()[0])
        max_val = max(matrix.row(0).tolist()[0])

        for i in range(1, matrix.rows):
            temp_row = matrix.row(i).tolist()[0]
            min_val = min(temp_row) if min(temp_row) < min_val else min_val
            max_val = max(temp_row) if max(temp_row) > max_val else max_val

        return max_val - min_val
