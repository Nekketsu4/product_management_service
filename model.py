from __future__ import annotations
from dataclasses import dataclass, asdict
import datetime
from typing import List


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
        """
        Возврашет True если есть такой товар в каталоге иначу False
        :param product: Product
        :return: bool
        """
        return product.article in self.products

    def can_subtract(self, product: Product):
        """
        Возвращает True если товара на складе больше чем то количество
        которое запрашивается пользователем
        :param product: Product
        :return: True otherwise raise ValueError
        """
        if not(self.has_product_in_catalog(product)
                    and self.products[product.article]['qty'] - product.qty >= 0):
            raise ValueError(f'На складе едостаточно товара: {product.name}')
        return True


    def add_product(self, product: Product):
        """
        Добавить товар на склад
        :param product: Product
        :return: bool
        """
        if not self.has_product_in_catalog(product):
            self.products.update({product.article: {
                'name': product.name,
                'qty': product.qty
            }})
        else:
            self.products[product.article]['qty'] += product.qty

    def subtract_product(self, product: Product):
        """
        Забрать товар со склада
        :param product:
        :return:
        """
        if self.can_subtract(product):
            self.products[product.article]['qty'] -= product.qty


def put_in_warehouse(warehouse: WareHouse, products: List[Product]):
    try:
        for product in products:
            warehouse.add_product(product)
        return products
    except Exception:
        raise Exception('Непредвиденная ошибка')

def get_from_warehouse(warehouse: WareHouse, products: List[Product]):
    try:
        for product in products:
            warehouse.subtract_product(product)
        return products
    except Exception:
        raise Exception('Непредвиденная ошибка')