import random
from collections import OrderedDict

from sympy import Matrix

random.seed(71)


def generate_random_matrix(rows: int, cols: int) -> Matrix:
    matrix = []

    for i in range(rows):
        row = [random.randrange(0, 1000) for _ in range(cols)]
        matrix.append([x / sum(row) for x in row])

    return Matrix(matrix)


def generate_opinions_vector(length: int, min_value: int = 1, max_value: int = 20) -> Matrix:
    return Matrix(
        [
            [
                float(random.randrange(min_value, max_value))
                for _ in range(length)
            ]
        ]
    )


def gennerate_influence(agents: int, min_value: int = -100, max_value: int = 100) -> OrderedDict:
    # Generate for first player
    first_player_agents_count = random.randint(1, agents-1)
    first_player_agents = random.sample(range(1, agents+1), first_player_agents_count)
    first_player_influence = float(random.randint(0, max_value))

    # Generate for second player
    second_player_agents_count = random.randint(1, agents-first_player_agents_count)
    second_player_agents = random.sample(
        set(range(1, agents + 1))-set(first_player_agents),
        second_player_agents_count
    )
    second_player_influence = float(random.randint(min_value, 0))

    return OrderedDict([
        (frozenset(first_player_agents), first_player_influence),
        (frozenset(second_player_agents), second_player_influence)
    ])


def add_influence_to_opinions_vector(opinions_vector: Matrix, influence_dict: OrderedDict) -> Matrix:
    for agents, influence in influence_dict.items():
        for agent in agents:
            opinions_vector[0, agent-1] = influence

    return opinions_vector
