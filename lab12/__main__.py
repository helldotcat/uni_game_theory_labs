from lab12.print import print_matrix, print_opinios_vector, print_influence
from lab12.solver import Solver
from lab12.utils import (
    generate_random_matrix,
    generate_opinions_vector,
    gennerate_influence,
    add_influence_to_opinions_vector,
)

N = 10


def main():
    print('РЕШЕНИЕ АНТАГОНИСТИЧЕСКОЙ ИГРЫ ИНФОРМАЦИОННОГО ПРОТИВОБОРСТВА\n')

    random_matrix = generate_random_matrix(N, N)
    print(f'\nСлучайная матрица доверия {N}x{N}:')
    print_matrix(random_matrix)

    solver = Solver(random_matrix)

    opinions_vector = generate_opinions_vector(N)
    print('\nИзначальные мнения агентов:')
    print_opinios_vector(opinions_vector)

    print('Расчёт мнений (без влияния).....\n')
    final_opinions, iterations = solver.get_final_opinions(opinions_vector)

    print(f'Потребовалось итераций: {iterations}')
    print('Результирующее мнение агентов (без влияния):')
    print_opinios_vector(final_opinions, iterations)

    print('\nГенерация агентов влияния и мнений.....\n')
    influence = gennerate_influence(N)
    print_influence(influence)

    print('Начальные мнения с учётом сформированных:')
    opinions_with_influence = add_influence_to_opinions_vector(opinions_vector, influence)
    print_opinios_vector(opinions_with_influence)

    print('Расчёт мнений (c влиянием).....\n')
    final_opinions, iterations = solver.get_final_opinions(opinions_with_influence)

    print(f'Потребовалось итераций: {iterations}')
    print('Результирующее мнение:')
    print_opinios_vector(final_opinions, iterations)


if __name__ == '__main__':
    main()
