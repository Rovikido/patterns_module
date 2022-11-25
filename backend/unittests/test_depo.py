import pytest
from random import *

from backend.classes.depo import *


def create_random_place_list(size):
    res = []
    for i in range(size):
        plc = Place(randrange(100), randrange(100), f'Place{i}')
        res.append(plc)

    return res


def create_random_item_list(size, place_list):
    res = []
    director = TransportItemDirector()
    for i in range(size):
        places = choices(place_list, k=2)
        chance = randrange(100) > 50
        director.set_builder(CargoBuilder) if chance else director.set_builder(PassengerCollectionBuilder)
        value = randint(1000, 10000) if chance else randint(20, 50)
        res.append(director.create_item(places[0], places[1], value))
    return res


def test_Depo():
    depo = Depo()
    places = create_random_place_list(5)

    route = depo.generate_route(places)

    items = create_random_item_list(20, places)
    for i in items:
        print(f'{i}\n')
        depo.add_item(i)

    factory = TransportFactory()
    plane = factory.create_transport(True, 'plane')

    delivered = depo.process_route(plane, route)

    assert delivered[0] in items
