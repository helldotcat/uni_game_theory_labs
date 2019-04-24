from lab8.sphere import Sphere


class Play:
    def __init__(self, sphere: Sphere):
        self.sphere = sphere
        self.result = None

    def run(self):
        self.sphere.generate_a_points()
        self.sphere.generate_b_point()

        self.result = self.sphere.find_intersection()

    def print_play(self):
        pass
