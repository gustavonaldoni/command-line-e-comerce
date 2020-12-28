from database.operations import ProductOperator
from terminaltables import AsciiTable

def show_all_products():
    operator = ProductOperator()

    column_names = ('Products', 'Prices(BRL)')
    all_products = operator.select_all_products_from_database()

    all_products.insert(0, column_names)

    table = AsciiTable(all_products)
    print(table.table)
    print()