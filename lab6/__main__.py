from analytical import AnalyticalSolver
from numerical import NumericalSolver


def main():
    input = [
     [1,  17,  18],
     [14,  6,  16],
     [14, 14,  13],
    ]


    # Compute analytical solution (Matrices multiplication)
    analytical_solver = AnalyticalSolver(input)

    game_cost = analytical_solver.calculate_game_cost()
    analytical_strategy_a = analytical_solver.calculate_strategy_a()
    analytical_strategy_b = analytical_solver.calculate_strategy_b()

    print("Analytical solution (Matrices multiplication)")
    print("Game cost: ", game_cost)
    print("Mixed strategy A: ", [x for x in analytical_strategy_a])
    print("Mixed strategy B: ", [x for x in analytical_strategy_b])


    # Compute numerical solution (Braun-Robinson algorithm)
    numerical_solver = NumericalSolver(input)

    numerical_strategy_a = numerical_solver.calculate_strategy_a()
    numerical_strategy_b = numerical_solver.calculate_strategy_b()

    print("\nNumerical solution (Braun-Robinson algorithm)")
    print("Mixed strategy A: ", [x for x in numerical_strategy_a])
    print("Mixed strategy B: ", [x for x in numerical_strategy_b])

    # Compare two methods (inaccuracy calculation)
    a_strategy_inaccuracy = [float(abs(x[0]-x[1])) for x in zip(analytical_strategy_a, numerical_strategy_a)]
    b_strategy_inaccuracy = [float(abs(x[0] - x[1])) for x in zip(analytical_strategy_b, numerical_strategy_b)]

    print("\nCompare two methods (inaccuracy calculation)")
    print("Inaccuracy for mixed strategies A: ", a_strategy_inaccuracy)
    print("Inaccuracy for mixed strategies B: ", b_strategy_inaccuracy)


if __name__ == "__main__":
    main()
