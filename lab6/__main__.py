from typing import List

from sympy import Rational

from lab6.analytical import AnalyticalSolver
from lab6.numerical import NumericalSolver


def strategy_to_str(name: str, strategy: List[Rational]):
    float_strategy = [float(x) - float(x) % 0.01 for x in strategy]

    return 'Mixed strategy {}: ['.format(name)\
           + ', '.join(['{:.2}'.format(x) for x in float_strategy])\
           + '],\tstrategy sum: {:.2}'.format(float(sum(strategy)))


def solve_analytical(input_matrix: List[List[int]]):
    # Compute analytical solution (Matrices multiplication)
    analytical_solver = AnalyticalSolver(input_matrix)

    game_cost = analytical_solver.calculate_game_cost()
    analytical_strategy_a = analytical_solver.calculate_strategy_a()
    analytical_strategy_b = analytical_solver.calculate_strategy_b()

    print('\n\nAnalytical solution (Matrices multiplication)'.upper())
    print(strategy_to_str('A', analytical_strategy_a))
    print(strategy_to_str('B', analytical_strategy_b))
    print('Game cost: {:.4}'.format(float(game_cost)))

    return analytical_strategy_a, analytical_strategy_b


def solve_numerical(input_matrix: List[List[int]]):
    # Compute numerical solution (Braun-Robinson algorithm)
    print('\n\nNumerical solution (Braun-Robinson algorithm)'.upper())

    numerical_solver = NumericalSolver(input_matrix)
    numerical_solver.solve()

    numerical_strategy_a = numerical_solver.calculate_strategy_a()
    numerical_strategy_b = numerical_solver.calculate_strategy_b()
    game_cost = numerical_solver.calculate_game_cost()

    print('\n' + strategy_to_str('A', numerical_strategy_a))
    print(strategy_to_str('B', numerical_strategy_b) + '\n')
    print('Game cost: {:.4}'.format(float(game_cost)))

    return numerical_strategy_a, numerical_strategy_b


def main():
    input_matrix = [
     [1,  17,  18],
     [14,  6,  16],
     [14, 14,  13],
    ]

    analytical_strategy_a, analytical_strategy_b = solve_analytical(input_matrix)
    numerical_strategy_a, numerical_strategy_b = solve_numerical(input_matrix)

    # Compare two methods (inaccuracy calculation)
    a_strategy_inaccuracy = [
        float(abs(x[0] - x[1]))
        for x in zip(analytical_strategy_a, numerical_strategy_a)
    ]
    b_strategy_inaccuracy = [
        float(abs(x[0] - x[1]))
        for x in zip(analytical_strategy_b, numerical_strategy_b)
    ]

    print('\n\nCompare two methods (inaccuracy calculation)'.upper())
    print('Inaccuracy for mixed strategies A: ',
          '['
          + ', '.join(['{:.2}'.format(x) for x in a_strategy_inaccuracy])
          + ']'
    )
    print('Inaccuracy for mixed strategies B: ',
          '['
          + ', '.join(['{:.2}'.format(x) for x in b_strategy_inaccuracy])
          + ']'
    )


if __name__ == '__main__':
    main()
