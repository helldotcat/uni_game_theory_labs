from sympy import Rational

from lab7.kernel_function import KernelFunction
from lab7.solvers.base_solver import NoSolutionException
from lab7.solvers.analytical_solver import AnalyticalSolver

import sys

def main():
    # kernel = KernelFunction(
    #     a=Rational(-10),
    #     b=Rational(15),
    #     c=Rational(60),
    #     d=Rational(-12),
    #     e=Rational(-48)
    # )
    kernel = KernelFunction(
        a=Rational(-3),
        b=Rational(3, 2),
        c=Rational(18, 5),
        d=Rational(-18, 50),
        e=Rational(-72, 25)
    )
    try:
        analytical_solver = AnalyticalSolver(kernel)
    except NoSolutionException as exception:
        print(exception)
        sys.exit(0)

    x_analytical, y_analytical = analytical_solver.solve()

    print(kernel.get_saddle_point(x_analytical, y_analytical))



    # print(kernel.H)
    # print(kernel.dH_dx)
    # print(kernel.dH_dx_dx)
    # print(kernel.dH_dy)
    # print(kernel.dH_dy_dy)
    # print(type(kernel.dH_dx))


if __name__ == '__main__':
    main()
