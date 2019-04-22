import random
from collections import OrderedDict

RANDOM_SEED = 20

random.seed(RANDOM_SEED)

RANDOM_PLAY_DIMENSION = 10, 10


def get_random_play():
    random_play = []
    for i in range(RANDOM_PLAY_DIMENSION[0]):
        random_play.append([
            (random.randint(-99, 99), random.randint(-99, 99))
            for _ in range(RANDOM_PLAY_DIMENSION[0])
        ])
    return random_play


CROSSROAD_PLAY = [
    [(1, 1), (1-0.01, 2)],
    [(2, 1-0.01), (0, 0)],
]


FAMILY_DISPUTE_PLAY = [
    [(4, 1), (0, 0)],
    [(0, 0), (1, 4)],
]


PRISONERS_DILEMMA_PLAY = [
    [(-5, -5), (0, -10)],
    [(-10, 0), (-1, -1)],
]

PLAY_BY_VARIANT = [
    [(2, 7), (8, 4)],
    [(1, 1), (11, 3)],
]

# PLAY_BY_VARIANT = [
#     [(3, 1), (5, 0)],
#     [(9, 6), (2, 3)],
# ]
#
# PLAY_BY_VARIANT = [
#     [(0, 1), (11, 4)],
#     [(7, 8), (6, 3)],
# ]

PLAYS = OrderedDict([
    ('Случайная 10x10', get_random_play()),
    ('Перекрёсток', CROSSROAD_PLAY),
    ('Семейный спор', FAMILY_DISPUTE_PLAY),
    ('Дилемма заключённого', PRISONERS_DILEMMA_PLAY),
    ('18 вариант', PLAY_BY_VARIANT),
])