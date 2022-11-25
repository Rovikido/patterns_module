import pytest

from backend.classes.transport import *
from backend.classes.places import *


def test_CargoPlane():
    factory = TransportFactory()
    res = factory.create_transport(False, 'plane')

    assert isinstance(res, CargoPlane)


def test_PassengerPlane():
    factory = TransportFactory()
    res = factory.create_transport(True, 'plane')

    assert isinstance(res, PassengerPlane)


def test_InvalidData():
    factory = TransportFactory()
    res = factory.create_transport(True, 'abcd')

    assert res == None