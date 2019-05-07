from sympy.matrices import Matrix
from lab9.utils import print_colored_matrix, BLUE_COLOR, YELLOW_COLOR, GREEN_COLOR, print_help, print_header
from lab9.solvers.nash_solver import NashSolver
from lab9.solvers.pareto_solver import ParetoSolver
from lab9.solvers.mixed_solver import MixedSolver
from lab9.play_matricies import PLAYS


def main():
    print_header()
    print_help()

    for play_name, play in PLAYS.items():
        print(f'Игра "{play_name.upper()}"\n')
        matrix_play = Matrix(play)

        nash_optimums = NashSolver(matrix_play).get_optimums()
        print_colored_matrix(Matrix(play), nash_optimums, BLUE_COLOR)

        pareto_optimums = ParetoSolver(matrix_play).get_optimums()
        print_colored_matrix(Matrix(play), pareto_optimums, YELLOW_COLOR)

        optimums_union = list(set(pareto_optimums) & set(nash_optimums))
        print_colored_matrix(Matrix(play), optimums_union, GREEN_COLOR)

        print('-'*120 + '\n\n\n')

    print('Поиск вполне смешанной ситуации равновесия...\n')

    mixed_solver = MixedSolver(Matrix(PLAYS['18 вариант']))

    mixed_solver.get_optimums()


if __name__ == '__main__':
    main()
