from rk3.characteristic_function import N, CHARACTERISTIC_FUNCTION as C_F, print_function
from rk3.convexity import check_convexity
from rk3.rationalization import check_group_rationalization, check_individual_rationalization
from rk3.superadditivity import check_superadditivity
from rk3.shepli import count_vector_shepli


def main():
    print('КООПЕРАТИВНЫЕ ИГРЫ: ВЕКТОР ШЕПЛИ\n')
    print_function()

    superadditivity_check_complete = False
    while not superadditivity_check_complete:
        superadditivity_check_complete = check_superadditivity()

        if not superadditivity_check_complete:
            new_key = frozenset((1, 2, 3, 4))
            new_value = 17

            print('Изменим характеристическую функцию: v({}) = {}\n'.format(set(new_key), new_value))

            C_F[new_key] = new_value

    check_convexity()

    vector_shepli = count_vector_shepli()

    check_group_rationalization(vector_shepli)

    check_individual_rationalization(vector_shepli)


if __name__ == '__main__':
    main()
