from rk3.characteristic_function import CHARACTERISTIC_FUNCTION as C_F


def check_superadditivity() -> bool:
    super_additivity = True
    checked_keys = set()

    for key in C_F.keys():
        keys_to_compare = set(C_F.keys()) - {key}

        for key_to_compare in keys_to_compare:
            keys_union = key_to_compare & key
            keys_intersection = key_to_compare | key

            if not keys_union and key_to_compare not in checked_keys:
                if C_F[keys_intersection] < C_F[key_to_compare] + C_F[key]:
                    print(
                        'Супераддитивность не выполняется на наборах {} и {}:'.format(
                            set(key_to_compare),
                            set(key))
                    )

                    print('v({}) < v({}) + v({})'.format(set(keys_intersection), set(key_to_compare), set(key)))
                    print('{} < {} + {}\n'.format(C_F[keys_intersection],  C_F[key_to_compare],  C_F[key]))
                    super_additivity = False

        checked_keys = checked_keys | {key}
    if super_additivity:
        print('Характеристическая функция супераддитивна')
    return super_additivity
