from dataclasses import dataclass, field


@dataclass
class Place:
    x: float
    y: float
    name: str = "None"

    def __str__(self):
        return f'{self.name}: {self.x}, {self.y}'


class Route:
    def __init__(self, route=[]):
        self.route = route

    def add_point(self, dest):
        self.route.append(dest)