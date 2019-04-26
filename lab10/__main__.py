from lab10.solver import Solver
from lab10.tree import Tree


def main():
    print(
        'ЛАБОРАТОРНАЯ РАБОТА 10.\nРЕШЕНИЕ ПОЗИЦИОННОЙ ИГРЫ С ПОЛНОЙ ИНФОРМАЦИЕЙ МЕТОДОМ ОБРАТНОЙ ИНДУКЦИИ\n'
        'Вариант 18\n'
    )

    tree = Tree()
    # tree.print_tree()

    solver = Solver(tree=tree)
    solver.solve()

    # tree.print_tree()
    tree.print_tree_horizontal()

    solver.print_results()


if __name__ == '__main__':
    main()
