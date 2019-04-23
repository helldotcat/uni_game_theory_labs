from rk3.characteristic_function import CHARACTERISTIC_FUNCTION as C_F


def check_convexity():
    print()
    checked_keys = set()
    is_convex = True

    for key in C_F.keys():
        keys_to_compare = set(C_F.keys()) - {key}

        for key_to_compare in keys_to_compare:
            if key_to_compare in checked_keys:
                continue

            keys_union = key_to_compare & key
            keys_intersection = key_to_compare | key

            if C_F[keys_intersection] + C_F[keys_union] < C_F[key_to_compare] + C_F[key]:
                print(
                    'Выпуклость не выполняется на наборах {} и {}:'.format(
                        set(key_to_compare),
                        set(key))
                )
                print('v({}) + v({}) < v({}) + v({})'.format(
                    set(keys_intersection), set(keys_union), set(key_to_compare), set(key))
                )
                print('{} + {} < {} + {}\n'.format(
                    C_F[keys_intersection], C_F[keys_union],  C_F[key_to_compare], C_F[key])
                )
                is_convex = False

        checked_keys = checked_keys | {key}

    if is_convex:
        print('Характеристическая функция выпуклая')

