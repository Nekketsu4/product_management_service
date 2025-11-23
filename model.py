from __future__ import annotations
from dataclasses import dataclass
import datetime


@dataclass(unsafe_hash=True)
class Product:
    article: str
    name: str
    qty: int



class WareHouse:
    def __init__(self, name):
        self.name = name
        self._products = list()
        self.time_of_action = datetime.datetime
        self.available_qty = 0

    def allocate(self, product: Product):
        self.available_qty += product.qty

    def deallocate(self, product: Product):
        self.available_qty -= product.qty

