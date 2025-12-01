import pytest

from model import Product, WareHouse


def test_if_exist_product_in_catalog():
    """
    Тест что товар есть в каталоге
    """
    catalog = WareHouse('warehouse')
    product = Product('product', 'TABLE', 20)

    catalog.add_product(product)
    assert catalog.has_product_in_catalog(product)

def test_can_add_qty_of_product():
    """
    Тест что можем добавить некоторое количество товаров
    на склад
    """
    catalog = WareHouse('warehouse')
    product = Product('product', 'TABLE', 20)

    catalog.add_product(product)
    assert catalog.products[product.article]['qty'] == 20

def test_can_add_many_times_qty_of_product():
    """
    Тест что можем добавить некоторое количество товаров
    несколько раз на склад
    """
    catalog = WareHouse('warehouse')
    product = Product('product', 'TABLE', 20)
    product1 = Product('product', 'TABLE', 50)

    catalog.add_product(product)
    catalog.add_product(product1)
    assert catalog.products[product.article]['qty'] == 70

def test_subtract_qty_of_product_from_warehouse():
    """
    Тесч что можно вычесть некоторое количество товаров из склада
    """
    catalog = WareHouse('warehouse')
    product = Product('product', 'TABLE', 20)
    catalog.add_product(product)

    product1 = Product('product', 'TABLE', 13)
    catalog.subtract_product(product1)
    assert catalog.products[product.article]['qty'] == 7

def test_error_subtract_qty_product_more_than_exist():
    """
    Тест вызывает исключение если запрашиваемое количество товара
    больше чем то, что есть на складе
    """
    catalog = WareHouse('warehouse')
    product = Product('product', 'TABLE', 20)
    catalog.add_product(product)

    product1 = Product('product', 'TABLE', 25)

    with pytest.raises(ValueError, match='На складе едостаточно товара: TABLE'):
        catalog.subtract_product(product1)