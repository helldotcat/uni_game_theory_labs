import math

from lab8.sphere import Sphere
from lab8.play import Play


class Solver:
    def __init__(self):
        self.plays = []
        self.plays_count = 100000
        self.a_points = 1
        self.max_distance = math.pi / 4

    def solve(self):
        for _ in range(self.plays_count):
            sphere = Sphere(self.a_points, self.max_distance)
            play = Play(sphere=sphere)
            play.run()
            self.plays.append(play)

    def print_results(self):
        print('Результаты игры:')
        print(f'Сделано {self.plays_count} розыгрешей')
        print('Выигрыши А: {0:2.2f} %'.format(self.a_wins / self.plays_count * 100))
        print('Выигрыши B: {0:2.2f} %'.format(self.b_wins / self.plays_count * 100))

    @property
    def play_results(self):
        return [play.result for play in self.plays]

    @property
    def a_wins(self):
        return len([result for result in self.play_results if not result])

    @property
    def b_wins(self):
        return len([result for result in self.play_results if result])
