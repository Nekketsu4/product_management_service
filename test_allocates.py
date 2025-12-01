from model import WareHouse, Product, put_in_warehouse, get_from_warehouse

def test_put_many_products_in_warehouse():
    """
    Тест что можем добавить сразу несколько товаров
    с разным количестом каждого из товаров
    """
    warehouse = WareHouse('warehouse1')
    tables = Product('product-111', 'TABLE', 25)
    chairs = Product('product-222', 'TALL-CHAIRS', 70)
    spoons = Product('product-34', 'SILVER-SPOON', 125)

    put_in_warehouse(warehouse, [tables, chairs, spoons])
    assert warehouse.products == {
        'product-111': {'name': 'TABLE', 'qty': 25},
        'product-222': {'name': 'TALL-CHAIRS', 'qty': 70},
        'product-34': {'name': 'SILVER-SPOON', 'qty': 125},
    }

def test_get_many_products_from_warehouse():
    """
    Тест что можем забрать сразу несколько товаров со склада
    с различным количеством каждого из товаров
    """
    warehouse = WareHouse('warehouse1')
    tables = Product('product-111', 'TABLE', 25)
    chairs = Product('product-222', 'TALL-CHAIRS', 70)
    spoons = Product('product-34', 'SILVER-SPOON', 125)

    put_in_warehouse(warehouse, [tables, chairs, spoons])

    get_tables = Product('product-111', 'TABLE', 10)
    get_spoons = Product('product-34', 'SILVER-SPOON', 70)

    get_from_warehouse(warehouse, [get_spoons, get_tables])

    assert warehouse.products == {
        'product-111': {'name': 'TABLE', 'qty': 15},
        'product-222': {'name': 'TALL-CHAIRS', 'qty': 70},
        'product-34': {'name': 'SILVER-SPOON', 'qty': 55},
    }
