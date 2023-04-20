class Product:
    def __init__(self, name: str, price: int, unit: float):
        self.name = name
        self.price = price
        self.unit = unit

    def __str__(self):
        return self.name

    def __float__(self):
        return self.price/100

    def __eq__(self, other):
        return self.name == other.name and self.unit == other.unit

    def get_total(self, quantity) -> int:
        return round(self.price * (quantity / self.unit))

class ShoppingCart:
    def __init__(self):
        self.products = []
        self.quantities = []

    def __bool__(self):
        return bool(self.products)

    def __eq__(self, other):
        return self.products == other.products and self.quantities == other.quantities

    def __float__(self):
        return self.get_total() / 100

    def __len__(self):
        return len(self.products)

    def __getitem__(self, item):
        return [str(self.products[item]), self.quantities[item]]

    def add_product(self, product, quantity) -> None:
        try:
            index = self.products.index(product)
            self.quantities[index] += quantity
        except ValueError:
            self.products.append(product)
            self.quantities.append(quantity)

    def remove_product(self, product) -> None:
        return self.products.remove(product)

    def sub_product(self, product, quantity) -> None:
        try:
            index = self.products.index(product)
            self.quantities[index] -= quantity
            if self.quantities[index] <= 0:
                self.products.remove(product)
        except ValueError:
            self.products.append(product)
            self.quantities.append(quantity)

    def get_total(self) -> int:
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.get_total(quantity)
        return total

class PaymentValidator:
    def is_valid(self):
        raise NotImplementedError


class PaymentProcessor:
    def purchase(self):
        raise NotImplementedError


class CashPaymentValidator(PaymentValidator):
    def is_valid(self):
        return True
