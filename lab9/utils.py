from colorama import Fore, Style
from typing import List, Union, Tuple
from sympy import Matrix, Integer, Float


RED_COLOR = Fore.RED
GREEN_COLOR = Fore.GREEN
BLUE_COLOR = Fore.BLUE
YELLOW_COLOR = Fore.YELLOW
BLACK_COLOR = Fore.BLACK


HEADER = '\nКРИТЕРИИ ВЫБОРА ОПТИМАЛЬНЫХ СТРАТЕГИЙ В НЕАНТАГОНИСТИЧЕСКИХ ИГРАХ И СВОЙСТВА ОПТИМАЛЬНЫХ РЕШЕНИЙ\n\n'


HELP_MESSAGE = f'''ПРАВИЛА ЦВЕТОВОГО КОДИРОВАНИЯ:

{BLUE_COLOR}синий цвет{Style.RESET_ALL} — равновесная ситуация по Нэшу
{YELLOW_COLOR}жёлтый цвет{Style.RESET_ALL} — отптимальная ситуация по Парето
{GREEN_COLOR}зелёный цвет{Style.RESET_ALL} — ситуация, равновесная по Нэшу и отптимальная по Парето

'''


def format_cell(cell: Union[Integer, Tuple[Integer, Integer], Tuple[Float, Float]]) -> str:
    if isinstance(cell, Integer):
        return '{:>3}'.format(int(cell))

    return '(' + \
           ', '.join(
               ['{:>4}'.format(int(num)) if isinstance(num, Integer) else '{:>3.2f}'.format(float(num)) for num in
                cell]
           ) + ')'


def print_colored_matrix(matrix: Matrix, color_ixs: List[Tuple[int, int]] = None, color: str = BLACK_COLOR) -> None:
    if not color_ixs:
        color_ixs = []

    res = '['
    for i in range(matrix.rows):
        res += ' ['
        res += ', '.join(
            [
                f'{color}{format_cell(matrix.row(i)[j])}{Style.RESET_ALL}' if (i, j) in color_ixs else format_cell(matrix.row(i)[j])
                for j in range(matrix.row(i).cols)
            ]
        )
        res += ']\n'
    res = res[:1] + res[2:-1] + ']\n'

    print(res)


def print_help():
    print(HELP_MESSAGE)


def print_header():
    print(HEADER)

