from model import Product, WareHouse


# def test_allocate_product_to_warehouse():
#     warehouse, product = create_product_and_warehouse(
#         'warehouse',
#         'product-1', 'Table', 5
#     )
#     warehouse.allocate(product)
#     assert warehouse.available_qty == 5
#
# def test_deallocate_product_to_warehouse():
#     warehouse, product = create_product_and_warehouse(
#         'warehouse',
#         'product-1', 'Table', 2
#     )
#     warehouse.deallocate(product)
#     assert warehouse.available_qty == 3

def test_if_exist_product_in_catalog():
    catalog = WareHouse('warehouse')
    product = Product('product', 'TABLE', 20)

    catalog.add_product(product)
    assert catalog.has_product_in_catalog(product)

def test_can_add_qty_of_product():
    catalog = WareHouse('warehouse')
    product = Product('product', 'TABLE', 20)

    catalog.add_product(product)
    assert catalog.products[product.article]['qty'] == 20

def test_can_add_many_times_qty_of_product():
    catalog = WareHouse('warehouse')
    product = Product('product', 'TABLE', 20)
    product1 = Product('product', 'TABLE', 50)

    catalog.add_product(product)
    catalog.add_product(product1)
    assert catalog.products[product.article]['qty'] == 70

def test_subtract_qty_of_product_from_warehouse():
    catalog = WareHouse('warehouse')
    product = Product('product', 'TABLE', 20)
    catalog.add_product(product)

    product1 = Product('product', 'TABLE', 13)
    catalog.subtract_product(product1)
    assert catalog.products[product.article]['qty'] == 7

def test_can_subtract_qty_of_product_from_warehouse():
    catalog = WareHouse('warehouse')
    product = Product('product', 'TABLE', 20)
    catalog.add_product(product)

    product1 = Product('product', 'TABLE', 25)
    catalog.subtract_product(product1)
    assert catalog.can_subtract(product1) is False