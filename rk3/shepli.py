from math import factorial as fact
from typing import List

from rk3.characteristic_function import N, CHARACTERISTIC_FUNCTION as C_F


def count_vector_shepli() -> List[float]:
    print()
    vector_shepli = []

    for i in range(1, N + 1):
        x_i_sum = 0
        for key in C_F.keys():
            if i in key:
                x_i_sum += fact(len(key) - 1) * fact(N-len(key)) * (C_F[key] - C_F[key - {i}])

        vector_shepli.append(x_i_sum/fact(N))

    print('Получен вектор Шепли: ' + '[' + ', '.join(['{0:.3f}'.format(x) for x in vector_shepli]) + ']')
    return vector_shepli
