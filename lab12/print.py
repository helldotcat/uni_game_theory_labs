from collections import OrderedDict

from sympy import Matrix


def print_matrix(matrix: Matrix) -> None:
    row_str = '['
    for i in range(matrix.rows):
        row_str += '[' + ', '.join(['{0:.3f}'.format(x) for x in matrix.row(i).tolist()[0]]) + '],\n '

    row_str = row_str[:-3] + ']'
    print(row_str)


def print_opinios_vector(vector: Matrix, iteration: int = 0) -> None:
    vector_str = 'x({})='.format(iteration)
    vector_str += '[' + ', '.join(['{0:.3f}'.format(x) for x in vector.row(0).tolist()[0]]) + ']\n'
    print(vector_str)


def print_influence(influence_dict: OrderedDict):
    player = 0
    for agents, inluence in influence_dict.items():
        player += 1
        print(f'Агенты игрока {player}: {tuple(sorted(agents))}')
        print('Сформированное начальное мнение агентов игрока {0}: {1:.0f}\n'.format(player, inluence))
