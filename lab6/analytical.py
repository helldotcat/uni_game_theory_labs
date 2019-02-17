from typing import List

from sympy import Rational
from sympy.matrices import Matrix, ones


class AnalyticalSolver:
    def __init__(self, input_matrix: List[List[int]]):
        self.payoff_matrix = Matrix(input_matrix)

    @property
    def inverse_payoff_matrix(self) -> Matrix:
        return self.payoff_matrix.inv()

    def calculate_strategy_a(self) -> Matrix:
        return ones(
            1, self.inverse_payoff_matrix.rows
        ).multiply(
            self.inverse_payoff_matrix
        ) * self.calculate_game_cost()

    def calculate_strategy_b(self) -> Matrix:
        return self.inverse_payoff_matrix.multiply(
            ones(self.inverse_payoff_matrix.cols, 1)
        ) * self.calculate_game_cost()

    def calculate_game_cost(self) -> Rational:
        return Rational(1) / ones(
            1, self.inverse_payoff_matrix.rows
        ).multiply(
            self.inverse_payoff_matrix
        ).multiply(
            ones(self.inverse_payoff_matrix.cols, 1)
        )[0]
