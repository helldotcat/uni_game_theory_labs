from lab9.solvers.nash_solver import NashSolver
from typing import List, Tuple
from sympy import Matrix, Rational, ones

from lab9.utils import print_colored_matrix, BLUE_COLOR


class MixedSolver(NashSolver):
    def get_optimums(self) -> List:
        a_strict_dominant_strategies = self.check_for_strict_dominant_strategy_a()
        b_strict_dominant_strategies = self.check_for_strict_dominant_strategy_b()
        nash_optimums = super().get_optimums()

        if a_strict_dominant_strategies or b_strict_dominant_strategies:
            print('Имеется строго доминирующая стратегия. Существует единственная ситуация равновесия по Нэшу.')
            print_colored_matrix(Matrix(self.matrix), nash_optimums, BLUE_COLOR)
            return nash_optimums

        print('Строго доминирующие стратегии не найдены.\n')
        if len(nash_optimums) == 0:
            print('Отсуствуют ситуации равновесия по Нэшу в чистых стратегиях.'
                  ' Существует вполне смешанная ситуация равновесия в смешанном дополнении.')
            self.print_mixed_strategies_and_gain()
            return nash_optimums

        if len(nash_optimums) == 2:
            print('Существуют две ситуации равновесия по Нэшу.')
            print_colored_matrix(Matrix(self.matrix), nash_optimums, BLUE_COLOR)

            print('Существует вполне смешанная ситуация равновесия в смешанном дополнении.')
            self.print_mixed_strategies_and_gain()
            return nash_optimums

    def print_mixed_strategies_and_gain(self) -> None:
        print('Стратегия игрока A :', self.strategy_a_str)
        print('Стратегия игрока B :', self.strategy_b_str, '\n')
        print('Равновесный выигрыш A: {0:.3f}'.format(self.gain_a))
        print('Равновесный выигрыш B: {0:.3f}'.format(self.gain_b))

    @property
    def matrix_a(self) -> Matrix:
        matrix_a = []
        for i in range(self.matrix.rows):
            matrix_a.append(
                [self.matrix.row(i)[j][0] for j in range(self.matrix.cols)]
            )
        return Matrix(matrix_a)

    @property
    def matrix_b(self) -> Matrix:
        matrix_b = []
        for i in range(self.matrix.rows):
            matrix_b.append(
                [self.matrix.row(i)[j][1] for j in range(self.matrix.cols)]
            )
        return Matrix(matrix_b)

    def calculate_strategy_a(self) -> Matrix:
        return ones(
            1, self.matrix_b.inv().rows
        ).multiply(
            self.matrix_b.inv()
        ) * self.calculate_game_cost_b()

    @property
    def strategy_a(self) -> List[float]:
        return [float(x) for x in self.calculate_strategy_a().row(0).tolist()[0]]

    @property
    def strategy_b(self) -> List[float]:
        return [float(x[0]) for x in self.calculate_strategy_b().col(0).tolist()]

    @property
    def strategy_a_str(self) -> str:
        return '[' + ', '.join(['{0:.3f}'.format(x) for x in self.strategy_a]) + ']'

    @property
    def strategy_b_str(self) -> str:
        return '[' + ', '.join(['{0:.3f}'.format(x) for x in self.strategy_b]) + ']'

    @property
    def gain_a(self) -> float:
        gain = 0
        for i in range(self.matrix_a.rows):
            for j in range(self.matrix_b.cols):
                gain += self.matrix_a.row(i)[j] * self.strategy_a[i] * self.strategy_b[j]
        return gain

    @property
    def gain_b(self) -> float:
        gain = 0
        for i in range(self.matrix_a.rows):
            for j in range(self.matrix_b.cols):
                gain += self.matrix_b.row(i)[j] * self.strategy_a[i] * self.strategy_b[j]
        return gain

    def calculate_strategy_b(self) -> Matrix:
        return self.matrix_a.inv().multiply(
            ones(self.matrix_a.inv().cols, 1)
        ) * self.calculate_game_cost_a()

    def calculate_game_cost_a(self) -> Rational:
        return Rational(1) / ones(
            1, self.matrix_a.inv().rows
        ).multiply(
            self.matrix_a.inv()
        ).multiply(
            ones(self.matrix_a.inv().cols, 1)
        )[0]

    def calculate_game_cost_b(self) -> Rational:
        return Rational(1) / ones(
            1, self.matrix_b.inv().rows
        ).multiply(
            self.matrix_b.inv()
        ).multiply(
            ones(self.matrix_b.inv().cols, 1)
        )[0]

    def check_for_strict_dominant_strategy_a(self) -> bool:
        for i in range(self.matrix_a.rows):
            for j in range(self.matrix_a.rows):
                if i != j:
                    i_row = self.matrix_a.row(i).tolist()[0]
                    j_row = self.matrix_a.row(j).tolist()[0]
                    if all([i_row[k] > j_row[k] for k in range(self.matrix_a.cols)]):
                        return True
        return False

    def check_for_strict_dominant_strategy_b(self) -> bool:
        for i in range(self.matrix_b.cols):
            for j in range(self.matrix_b.cols):
                if i != j:
                    i_col = [x[0] for x in self.matrix_b.col(i).tolist()]
                    j_col = [x[0] for x in self.matrix_b.col(j).tolist()]
                    if all([i_col[k] > j_col[k] for k in range(self.matrix_b.cols)]):
                        return True
        return False


