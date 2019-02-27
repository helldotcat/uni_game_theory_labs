import sys

from sympy import Rational

from lab7.kernel_function import KernelFunction
from lab7.solvers.analytical_solver import AnalyticalSolver
from lab7.solvers.base_solver import NoSolutionException
from lab7.solvers.numerical_solver import NumericalSolver


def compute_analytical_solution(kernel_function: KernelFunction):
    try:
        analytical_solver = AnalyticalSolver(kernel_function)
    except NoSolutionException as exception:
        print(exception)
        sys.exit(0)

    x, y, H = analytical_solver.solve()

    print('АНАЛИТИЧЕСКОЕ РЕШЕНИЕ')
    print('x={:2.3f} y={:2.3f} H={:2.3f}\n\n'.format(float(x), float(y), float(H)))


def compute_numerical_solution(kernel_function: KernelFunction):
    print('ЧИСЛЕННОЕ РЕШЕНИЕ')
    try:
        for steps in range(2, 11):
            print(f'N={steps}')
            numerical_solver = NumericalSolver(kernel_function, steps)
            print(numerical_solver.matrix_to_str())

            x, y, H = numerical_solver.solve()
            print('x={:2.3f} y={:2.3f} H={:2.3f}\n\n'.format(float(x), float(y), float(H)))

    except NoSolutionException as exception:
        print(exception)
        sys.exit(0)


def main():
    kernel = KernelFunction(
        a=Rational(-10),
        b=Rational(15),
        c=Rational(60),
        d=Rational(-12),
        e=Rational(-48)
    )
    # kernel = KernelFunction(
    #     a=Rational(-3),
    #     b=Rational(3, 2),
    #     c=Rational(18, 5),
    #     d=Rational(-18, 50),
    #     e=Rational(-72, 25)
    # )

    compute_analytical_solution(kernel)

    compute_numerical_solution(kernel)


if __name__ == '__main__':
    main()
