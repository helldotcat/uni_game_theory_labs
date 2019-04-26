from pptree import print_tree
from typing import List, Iterable
import random
from pprint import pprint


random.seed(43)


class Vertex:
    def __init__(self, player: int = None, parent = None):
        self.ix = None
        self.player = player
        self.gains = []
        self.children = []
        self.parent = parent

        if self.parent:
            self.parent.children.append(self)

    def __str__(self):
        str_res = str(self.gains) if len(self.gains) != 1 else str(self.gains[0])
        if self.player:
            return '─ {:<12s} {:>1s} ─'.format(str_res, str(self.player))

        return f' {str_res}'


class Tree:
    def __init__(self):
        self.depth = 7
        self.gain_range = 0, 15
        self.players = 3
        self.strategies = 2, 2, 2

        self.root = None

        self._generate_tree()

    def _generate_tree(self):
        self.root = Vertex(player=self.step_oder[0])
        ix = 0

        for i in range(self.depth):
            vertexes_on_i_level = self._get_vertex_on_level(i)
            for vertexes_series in vertexes_on_i_level:
                for vertex in vertexes_series:
                    for new_child in self._generate_children_for_level(i):
                        new_child.ix = ix
                        ix += 1
                        new_child.parent = vertex
                        vertex.children.append(new_child)

    def _generate_children_for_level(self, level: int) -> Iterable[Vertex]:
        player = self.step_oder[level]
        for _ in range(self.strategies[player-1]):
            if level + 1 == self.depth:
                next_vertex = Vertex()
                next_vertex.gains = [tuple([random.randint(self.gain_range[0], self.gain_range[1])
                                     for _ in range(self.players)])]
            else:
                next_vertex = Vertex(player=self.step_oder[level+1])
            yield next_vertex

    def _get_vertex_on_level(self, level: int) -> List[List[Vertex]]:
        if level == 0:
            return [[self.root]]

        vertexes_on_level = []
        temp_vertex = self.root
        temp_depth = 0
        visited = {id(temp_vertex)}

        while temp_vertex:
            current_vertex = temp_vertex
            for child in temp_vertex.children:
                if id(child) not in visited:
                    temp_vertex = child
                    temp_depth += 1
                    break

            if current_vertex is temp_vertex:
                if temp_depth == level - 1:
                    vertexes_on_level.append(temp_vertex.children)

                visited.add(id(temp_vertex))
                temp_depth -= 1
                temp_vertex = temp_vertex.parent

        return vertexes_on_level

    def make_reversed_induction_step(self, level: int) -> None:
        vertexes_on_level = self._get_vertex_on_level(level)
        player = self.step_oder[level]

        for vertexes_series in vertexes_on_level:
            for vertex in vertexes_series:
                strategies_to_compare = []
                for child in vertex.children:
                    if isinstance(child.gains, list):
                        strategies_to_compare += child.gains
                    else:
                        strategies_to_compare += [child.gains]

                top_strategy = max(strategies_to_compare, key=lambda x: x[player-1])

                vertex.gains = [strategy for strategy in strategies_to_compare
                                if strategy[player-1] == top_strategy[player-1]]

        # self.print_tree()


    @property
    def step_oder(self) -> List[int]:
        return [(i % self.players) + 1 for i in range(self.depth)]

    def print_tree(self):
        print_tree(self.root, childattr='children')

    def print_tree_horizontal(self):
        matrix = []
        matrix_grid = []
        print_grid = self._generate_print_grid()
        pprint(print_grid)

        # for level in list(reversed(range(self.depth+1))):
        #     vertexes_on_level = self._get_vertex_on_level(level)
        #     matrix_level = [[]]
        #     matrix_grid.append([])
        #
        #     for vertexes_series in vertexes_on_level:
        #         for vertex in vertexes_series:
        #             cell_height = len(vertex.gains)
        #             cell_width = len(str(vertex.gains))
        #             matrix_grid[-1].append((cell_width, cell_height))
        #             # max_len = max([len(str(x)) for x in vertex.gains])
        #             # string_matrix_level[0].append(str(vertex.gains))
        #
        #     matrix += matrix_level
        #
        # pprint(matrix_grid)
        # self._print_string_matrix(matrix)

    def _generate_print_grid(self):
        length_table = []
        max_column_len = len('(, , )')
        max_column_len += self.players * max([len(str(x)) for x in range(self.gain_range[0], self.gain_range[1])])

        for level in range(self.depth+1):
            vertex_on_level = sum([len(vertexes_series) for vertexes_series in self._get_vertex_on_level(level)])
            length_table.append([max_column_len for _ in range(vertex_on_level)])

        grid = []

        max_row_length = max([sum(length_row) for length_row in length_table])
        for length_row in length_table:

        return grid

    def print_in_cell(self, width: int, height: int, text: str):
        text_rows = text.split('\n')
        padding_rows_count = height - len(text_rows)
        rows_before = rows_after = 0
        if padding_rows_count:
            rows_before = rows_after = int(padding_rows_count / 2)
            if padding_rows_count % 2 == 1:
                rows_before += 1
        result_str = ''

        for _ in range(rows_before):
            result_str += ' ' * width + '\n'

        format_str = '{:^'+ str(width) +'s}'
        for text_row in text_rows:
            result_str += format_str.format(text_row) + '\n'

        for _ in range(rows_after):
            result_str += ' ' * width + '\n'

        return result_str


    def _print_string_matrix(self, print_matrix: List[List[str]]):
        for row in print_matrix:
            print(''.join(row))

