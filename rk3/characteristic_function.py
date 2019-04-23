from collections import OrderedDict


CHARACTERISTIC_FUNCTION = OrderedDict([
    (frozenset(),             0),
    (frozenset((1, )),        2),
    (frozenset((2, )),        3),
    (frozenset((3, )),        4),
    (frozenset((4, )),        4),

    (frozenset((1, 2)),       6),
    (frozenset((1, 3)),       6),
    (frozenset((1, 4)),       7),
    (frozenset((2, 3)),       7),
    (frozenset((2, 4)),       8),
    (frozenset((3, 4)),       8),

    (frozenset((1, 2, 3)),    11),
    (frozenset((1, 2, 4)),    11),
    (frozenset((1, 3, 4)),    12),
    (frozenset((2, 3, 4)),    12),

    (frozenset((1, 2, 3, 4)), 14),
    # (frozenset((1, 2, 3, 4)), 15),
])

# CHARACTERISTIC_FUNCTION = OrderedDict([
#     (frozenset(),             0),
#     (frozenset((1, )),        1),
#     (frozenset((2, )),        1),
#     (frozenset((3, )),        1),
#
#     (frozenset((1, 2)),       3),
#     (frozenset((1, 3)),       3),
#     (frozenset((2, 3)),       3),
#
#     (frozenset((1, 2, 3)),    4),
# ])

N = max(len(key) for key in CHARACTERISTIC_FUNCTION.keys())


def print_function():
    print('Дана характеристическая функция')
    for key in CHARACTERISTIC_FUNCTION.keys():
        print('v({}) = {}'.format(set(key) if key else '{}', CHARACTERISTIC_FUNCTION[key]))
    print()
