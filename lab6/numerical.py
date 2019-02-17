from collections import defaultdict
from typing import List, Tuple, Callable, Optional

from sympy import Rational
from sympy.matrices import Matrix


class NumericalSolver:
    def __init__(self, input_matrix: List[List[int]]):
        self.payoff_matrix = Matrix(input_matrix)

    def calculate_strategy_a(self):
        braun_robinson_table = BraunRobinsonTable(
            self.payoff_matrix,
            self.get_maximin()[1][0],
            self.get_minimax()[1][1],
        )

        braun_robinson_table.solve(0.1)
        return braun_robinson_table.get_a_mixed_strategy()

    def calculate_strategy_b(self):
        braun_robinson_table = BraunRobinsonTable(
            self.payoff_matrix,
            self.get_maximin()[1][0],
            self.get_minimax()[1][1],
        )
        braun_robinson_table.solve(0.1)
        return braun_robinson_table.get_b_mixed_strategy()

    def get_maximin(self) -> Tuple[int, Tuple[int, int]]:
        mins_by_rows = self._find_extremums_by_axis('rows', fn=min)
        maximum = max(mins_by_rows, key=lambda x: x[0])

        return maximum[0], (mins_by_rows.index(maximum), maximum[1])

    def get_minimax(self) -> Tuple[int, Tuple[int, int]]:
        maxs_by_cols = self._find_extremums_by_axis('columns', fn=max)
        minimum = min(maxs_by_cols, key=lambda x: x[0])

        return minimum[0], (minimum[1], maxs_by_cols.index(minimum))

    def _find_extremums_by_axis(self, axis: str, fn: Callable) -> List[Tuple[int, int]]:
        if axis == 'columns':
            lines = [self.payoff_matrix.col(j).T.tolist()[0] for j in range(self.payoff_matrix.cols)]
        elif axis == 'rows':
            lines = [self.payoff_matrix.row(i).tolist()[0] for i in range(self.payoff_matrix.rows)]
        else:
            raise Exception("Axis should be 'rows' or 'columns'")

        return [(fn(line), line.index(fn(line))) for line in lines]


class BraunRobinsonAlgorithmStep:
    def __init__(
            self,
            a_choice: int,
            b_choice: int,
            payoff_matrix: Matrix,
            previous_step: Optional):
        self.step_number = previous_step.step_number + 1 if previous_step else 1
        self.a_choice = a_choice
        self.b_choice = b_choice

        self.a_gain = payoff_matrix.col(self.b_choice).T.tolist()[0]
        self.b_gain = payoff_matrix.row(self.a_choice).tolist()[0]
        if previous_step:
            self.a_gain = [sum(x) for x in zip(self.a_gain, previous_step.a_gain)]
            self.b_gain = [sum(x) for x in zip(self.b_gain, previous_step.b_gain)]

    @property
    def upper_game_cost(self) -> Rational:
        return max(self.a_gain)/Rational(self.step_number)

    @property
    def lower_game_cost(self) -> Rational:
        return min(self.b_gain) / Rational(self.step_number)

    @property
    def epsilon(self) -> Rational:
        return self.upper_game_cost - self.lower_game_cost

    def __str__(self):
        return f'{self.a_choice}|{self.b_choice}|{self.a_gain}|{self.b_gain}|' \
            f'{self.lower_game_cost}|{self.upper_game_cost}|{float(self.epsilon)}'


class BraunRobinsonTable:
    def __init__(self, payoff_matrix: Matrix, first_a: int, first_b: int):
        self.payoff_matrix = payoff_matrix
        self.steps = []

        self.make_step(first_a, first_b)
        print(self.steps[-1])

    def solve(self, threshold: float = 0.01, max_steps: int = 2**64):
        while threshold < self.steps[-1].epsilon and max_steps > len(self.steps):
            self.make_step()
            print(self.steps[-1])

    def make_step(self, a_strategy: int = None, b_strategy: int = None):
        if all([a_strategy is None, b_strategy is None]):
            a_strategy = self._get_next_a_strategy()
            b_strategy = self._get_next_b_strategy()
        elif any([a_strategy is None, b_strategy is None]):
            raise Exception(
                'Both strategy should be defined or should be None. Gor strategies: %s', [a_strategy, b_strategy]
            )

        step = BraunRobinsonAlgorithmStep(
            a_choice=a_strategy,
            b_choice=b_strategy,
            payoff_matrix=self.payoff_matrix,
            previous_step=self.steps[-1] if self.steps else None
        )
        self.steps.append(step)

    def get_a_mixed_strategy(self):
        counter = defaultdict(int)
        for step in self.steps:
            counter[step.a_choice] += 1

        return [Rational(counter[choice], len(self.steps)) for choice in sorted(counter.keys())]

    def get_b_mixed_strategy(self):
        counter = defaultdict(int)
        for step in self.steps:
            counter[step.b_choice] += 1

        return [Rational(counter[choice], len(self.steps)) for choice in sorted(counter.keys())]

    def _get_next_a_strategy(self) -> int:
        max_from_previous_a_gain = max(self.steps[-1].a_gain)

        if len(self.steps) > 1 and self.steps[-2].a_gain[self.steps[-1].a_choice] == max_from_previous_a_gain:
            return self.steps[-1].a_choice

        return self.steps[-1].a_gain.index(max_from_previous_a_gain)

    def _get_next_b_strategy(self) -> int:
        min_from_previous_b_gain = min(self.steps[-1].b_gain)

        if len(self.steps) > 1 and self.steps[-2].b_gain[self.steps[-1].b_choice] == min_from_previous_b_gain:
            return self.steps[-1].b_choice

        return self.steps[-1].b_gain.index(min_from_previous_b_gain)
