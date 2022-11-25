from dataclasses import dataclass, field
from abc import ABCMeta, abstractmethod


class TransportItem:
    def __init__(self):
        self.src_place = None
        self.target_place = None
        self.weight = 0
        self.passenger_num = 0

    def __str__(self):
        return f'Item with {self.weight} weight and {self.passenger_num} passengers'


class TransportItemBuilder(metaclass=ABCMeta):
    @abstractmethod
    def add_weight(self, value: int):
        pass

    @abstractmethod
    def add_passenger_num(self, value: int):
        pass


class CargoBuilder(TransportItemBuilder):
    def __init__(self):
        self.obj = TransportItem()

    def reset(self):
        self.obj = TransportItem()

    def get_transport(self):
        res = self.obj
        self.reset()
        return res

    def add_places(self, src_place, target_place):
        self.obj.src_place = src_place
        self.obj.target_place = target_place

    def add_weight(self, value: int):
        self.obj.weight = value

    def add_passenger_num(self, value: int = 0):
        pass


class PassengerCollectionBuilder(TransportItemBuilder):
    def __init__(self):
        self.obj = TransportItem()

    def reset(self):
        self.obj = TransportItem()

    def get_transport(self):
        res = self.obj
        self.reset()
        return res

    def add_places(self, src_place, target_place):
        self.obj.src_place = src_place
        self.obj.target_place = target_place

    def add_weight(self, value: int = 0):
        pass

    def add_passenger_num(self, value: int):
        self.obj.passenger_num = value


class TransportItemDirector:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder()

    def create_item(self, src_place, target_place, value):
        self.builder.add_places(src_place, target_place)
        self.builder.add_weight(value)
        self.builder.add_passenger_num(value)
        return self.builder.get_transport()
