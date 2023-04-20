class Product:
    name: str = 'name'
    price: int = 0
    unit: float = 0.1

    def get_total(self, unit_prod=unit) -> int:
        total_price: float = self.price * unit_prod / self.unit
        return int(total_price)


product1 = Product()
product1.name = 'apple'
product1.price = 1059
product1.unit = 0.1
print(product1.get_total(0.7))
print(product1.get_total())


class Product:
    name: str = 'name'
    price: int = 0
    unit: float = 0.1

    def get_total(self, unit_prod=unit) -> int:
        total_price: float = self.price * unit_prod / self.unit
        return int(total_price)


class ShoppingCart:
    products: list = []
    quantities: list = []

    def add_product(self, product, unit_prod=1) -> None:
        if unit_prod is None:
            unit_prod = product.unit
        self.products.append(product)
        self.quantities.append(unit_prod)

    def get_total(self) -> int:
        total_prod: list = []
        for i in range(len(self.products)):
            total_prod.append((self.products[i].price / self.products[i].unit) * self.quantities[i])
        return int(sum(total_prod))


product_obj = Product()
product_obj.name = "juice"
product_obj.price = 3655
product_obj.unit = 1
cart_obj = ShoppingCart()
cart_obj.add_product(product_obj, 3)  # put 3 packs of juice to cart
cart_obj.add_product(product_obj)     # add one more (unit = 1)
cart_obj.get_total()           # == 14620 , 3655 x 4




class Product:

    def __init__(self, name, price, unit):
        self.name = name
        self.price = price
        self.unit = unit

    def __str__(self) -> str:
        return self.name

    def __float__(self) -> float:
        return self.price / 100

    def __eq__(self, other) -> bool:
        return self.name == other.name and\
            self.price == other.price and self.unit == other.unit


    def get_total(self, unit_product) -> int:
        total_price: float = self.price * unit_product / self.unit
        return int(total_price)



class ShoppingCart:

    def __init__(self):
        self.products = []
        self.quantities = []
        self.index = 0

    def __float__(self) -> float:
        return self.get_total / 100


    def __eq__(self, other) -> bool:
        return self.products == other.products and\
            self.quantities == other.quantities


    def add_product(self, product, unit_prod: float = 1) -> None:
        if unit_prod is None:
           unit_prod = product.unit
        self.products.append(product)
        self.quantities.append(unit_prod)

    def get_total(self) -> int:
        amount_product: list = []
        for item in range(len(self.products)):
            amount_product.append((self.products[item].price / self.products[item].unit) * self.quantities[item])
        return int(sum(amount_product))


candy = Product("candy", 1059, 0.1)
sweet = Product("candy", 1059, 0.1)
juice = Product("juice", 3655, 1)
cart_1 = ShoppingCart()
cart_2 = ShoppingCart()
cart_1.add_product(candy, 1)
cart_1.add_product(sweet, 0.5)
cart_2.add_product(juice)
assert cart_1.get_total  # == 15885
assert str(candy)                  # == "candy"
assert float(candy)                # == 10.59
assert float(cart_1)               # == 36.55
assert candy == sweet
assert sweet != juice
assert cart_1