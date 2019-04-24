from lab8.solver import Solver


def main():
    print('ЛАБОРАТОРНАЯ РАБОТА 8: ИГРА НА СФЕРЕ.\n')

    solver = Solver()
    solver.solve()

    solver.plays[0].sphere.print_sphere()
    solver.print_results()


if __name__ == '__main__':
    main()
