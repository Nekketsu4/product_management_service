from __future__ import annotations
from dataclasses import dataclass, asdict
import datetime


@dataclass
class Product:
    article: str
    name: str
    qty: int


class WareHouse:
    def __init__(self, name):
        self.name = name
        self.products = dict()
        self.time_of_action = datetime.datetime

    def has_product_in_catalog(self, product: Product):
        return product.article in self.products

    def can_subtract(self, product: Product):
        return (self.has_product_in_catalog(product)
                and self.products[product.article]['qty'] - product.qty >= 0)

    def add_product(self, product: Product):
        if not self.has_product_in_catalog(product):
            self.products.update({product.article: asdict(product)})
        else:
            self.products[product.article]['qty'] += product.qty

    def subtract_product(self, product: Product):
        if self.can_subtract(product):
            self.products[product.article]['qty'] -= product.qty

