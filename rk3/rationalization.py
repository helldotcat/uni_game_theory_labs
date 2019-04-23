from typing import List

from rk3.characteristic_function import N, CHARACTERISTIC_FUNCTION as C_F


def check_individual_rationalization(vector_shepli: List[float]):
    print()
    for i in range(1, N+1):
        if vector_shepli[i-1] >= C_F[frozenset([i])]:
            print(
                'Индивидуальная рационализация для игрока {0} выполняется: {1:.3f} >= {2:.3f}'.format(
                    i,
                    vector_shepli[i - 1],
                    C_F[frozenset([i])]
                )
            )
        else:
            print(
                'Индивидуальная рационализация для игрока {0} не выполняется: {1:.3f} >= {2:.3f}'.format(
                    i,
                    vector_shepli[i - 1],
                    C_F[frozenset([i])]
                )
            )


def check_group_rationalization(vector_shepli: List[float]):
    print()
    if sum(vector_shepli) == C_F[frozenset([i for i in range(1, N+1)])]:
        print(
            'Групповая рационализация выполняется: {0:.3f} == {0:.3f}'.format(
                sum(vector_shepli),
                C_F[frozenset([i for i in range(1, N+1)])]
            )
        )

        return

    print(
        'Групповая рационализация не выполняется: {0:.3f} == {0:.3f}'.format(
            sum(vector_shepli),
            C_F[frozenset([i for i in range(1, N + 1)])]
        )
    )
