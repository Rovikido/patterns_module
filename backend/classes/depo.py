from math import sqrt
from backend.classes.items import *
from backend.classes.transport import *
from backend.classes.places import *


class Depo:
    def __init__(self):
        self.hub = Place(0, 0, 'Hub')
        self.transport_item_list = []

    def add_item(self, item):
        self.transport_item_list.append(item)

    def generate_route(self, destination_list: [Place]):
        route = Route([destination_list[0]])
        prev_place = destination_list[0]
        for dest in destination_list[1:]:
            if self.calc_distance(prev_place, dest) > self.calc_distance(prev_place, self.hub) + self.calc_distance(self.hub, dest):
                route.add_point(self.hub)
                route.add_point(dest)
            else:
                route.add_point(dest)
        route.add_point(destination_list[0])
        return route

    def process_route(self, transport_obj: Transport, rout):
        route = rout.route
        delivered_packages = []
        for i in range(len(route)):
            place = route[i]
            for item in [x for x in transport_obj.cargo_list if x.target_place == place]:
                transport_obj.drop_cargo(item)
                delivered_packages.append(item)
            available_cargo = [x for x in self.transport_item_list if x.src_place == place and x.target_place in route[i+1:]]
            for item in available_cargo:
                if item.passenger_num+transport_obj.cur_passengers < transport_obj.max_passengers and item.weight+transport_obj.cur_cargo < transport_obj.max_tonnage:
                    transport_obj.add_cargo(item)
                    self.transport_item_list.remove(item)
        return delivered_packages

    def calc_distance(self, place1, place2):
        return sqrt((place1.x - place2.x)**2 + (place1.y - place2.y)**2)


