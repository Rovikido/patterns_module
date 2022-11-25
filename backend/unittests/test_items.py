import pytest

from backend.classes.items import *
from backend.classes.places import *


def test_CargoItemBuilder():
    director = TransportItemDirector()
    director.set_builder(CargoBuilder)
    src_place = Place(0, 5, "Place1")
    trg_place = Place(10, 20, "Place2")
    value = 5
    res = director.create_item(src_place, trg_place, value)

    assert res.src_place == src_place
    assert res.target_place == trg_place
    assert res.weight == value


def test_PassengerCollectionBuilder():
    director = TransportItemDirector()
    director.set_builder(PassengerCollectionBuilder)
    src_place = Place(0, 5, "Place1")
    trg_place = Place(10, 20, "Place2")
    value = 5
    res = director.create_item(src_place, trg_place, value)

    assert res.src_place == src_place
    assert res.target_place == trg_place
    assert res.passenger_num == value
