from typing import NamedTuple
import random
import math
from math import sqrt, sin, cos


random.seed(88)


class Point(NamedTuple):
    phi: float
    lbda: float


class Sphere:
    def __init__(self, a_points_count: int, max_distance: float):
        self.a_points_count = a_points_count
        self.max_distance = max_distance

        self.a_points = []
        self.b_point = None

    def print_sphere(self):
        print('Сфера:')
        print(f'Число противоракет у игрока A: {self.a_points_count}')
        print(f'Радиус поражения противоракет: {self.max_distance}\n')

    def generate_a_points(self) -> None:
        for _ in range(self.a_points_count):
            self.a_points.append(self._generate_random_point())

    def generate_b_point(self) -> None:
        self.b_point = self._generate_random_point()

    def find_intersection(self) -> bool:
        for point in self.a_points:
            distance = self._calculate_distance(point, self.b_point)

            if distance < self.max_distance:
                return True
        return False

    def _generate_random_point(self) -> Point:
        random_z = random.uniform(-1, 1)
        phi = math.asin(random_z)
        lbd = random.uniform(0, 2*math.pi)

        if lbd == 2 * math.pi:
            lbd = 0

        return Point(phi, lbd)

    def _calculate_distance(self, a_point: Point, b_point: Point) -> float:
        a_phi = a_point.phi
        b_phi = b_point.phi

        a_lbd = a_point.lbda
        b_lbd = b_point.lbda

        return abs(
            math.atan(
                sqrt(
                    (cos(b_phi)*sin(abs(a_lbd-b_lbd))) ** 2 +
                    (cos(a_phi)*sin(b_phi) - sin(a_phi)*cos(b_phi)*cos(abs(a_lbd-b_lbd))) ** 2
                )/(sin(a_phi)*sin(b_phi) + cos(a_phi)*cos(b_phi)*cos(abs(a_lbd-b_lbd)))
            )
        )
