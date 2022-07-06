from __future__ import annotations
from abc import ABC, abstractmethod


class Logistics(ABC):
    @abstractmethod
    def createTransport(self):
        pass

    def planDelivery(self):
        product = self.createTransport()
        transport = product.operation()
        return transport


class RoadLogistics(Logistics):
    def createTransport(self) -> Product:
        return Truck()


class ShipLogistics(Logistics):
    def createTransport(self) -> Product:
        return Ship()


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Truck(Product):
    def operation(self) -> str:
        return 'Caminhão entrega por terra'


class Ship(Product):
    def operation(self) -> str:
        return 'Navio entrega por água'


def Client(creator: Logistics) -> None:
    return creator.planDelivery()


if __name__ == '__main__':
    truck = Client(RoadLogistics())
    print(truck)
    ship = Client(ShipLogistics())
    print(ship)
