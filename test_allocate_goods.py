from model import Product, WareHouse

def create_product_and_warehouse(
        warehouse_name, product_article,
        product_name, qty
):
    return (
        WareHouse(warehouse_name),
        Product(product_article, product_name, qty)
    )

def test_allocate_product_to_warehouse():
    warehouse, product = create_product_and_warehouse(
        'warehouse',
        'product-1', 'Table', 5
    )
    warehouse.allocate(product)
    assert warehouse.available_qty == 5

def test_deallocate_product_to_warehouse():
    warehouse, product = create_product_and_warehouse(
        'warehouse',
        'product-1', 'Table', 2
    )
    warehouse.deallocate(product)
    assert warehouse.available_qty == 3