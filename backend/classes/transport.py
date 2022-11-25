from dataclasses import dataclass, field
from abc import ABCMeta, abstractmethod


class Transport:
    def __init__(self):
        self.max_tonnage = 0
        self.max_passengers = 0
        self.cur_cargo = 0
        self.cur_passengers = 0
        self.cargo_list = []

    def add_cargo(self, item):
        self.cur_cargo += item.weight
        self.cur_passengers += item.passenger_num
        print(f'Item {item} was picked up at {item.src_place}')
        self.cargo_list.append(item)

    def drop_cargo(self, item):
        self.cur_cargo -= item.weight
        self.cur_passengers -= item.passenger_num
        print(f'Item {item} was dropped at {item.target_place}')
        self.cargo_list.remove(item)


class PassengerPlane(Transport):
    def __init__(self):
        super().__init__()
        self.max_tonnage = 12 * 1000
        self.max_passengers = 225
        self.cur_cargo = 0
        self.cur_passengers = 0


class CargoPlane(Transport):
    def __init__(self):
        super().__init__()
        self.max_tonnage = 75 * 1000
        self.max_passengers = 0
        self.cur_cargo = 0
        self.cur_passengers = 0


class TransportFactory:
    def create_transport(self, is_passenger=False, type='plane'):
        if type == 'plane':
            return PassengerPlane() if is_passenger else CargoPlane()

        return None
