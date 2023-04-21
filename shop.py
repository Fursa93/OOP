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

    def __eq__(self, other):
        return self.products == other.products and self.quantities == other.quantities

    def __float__(self):
        return self.get_total() / 100

    def __len__(self):
        return len(self.products)

    def __getitem__(self, item) -> tuple:
        return self.products[item], self.quantities[item]

    def add_product(self, product, quantity) -> None:
        try:
            index = self.products.index(product)
            self.quantities[index] += quantity
        except ValueError:
            self.products.append(product)
            self.quantities.append(quantity)

    def remove_product(self, product) -> None:
         if product in self.products:
            index_product = self.products.index(product)
            self.products.pop(index_product)
            self.quantities.pop(index_product)
         else:
            print('We apologize, but unfortunately we do not have this product')

    def sub_product(self, product,  quantity):
        index_product = self.products.index(product)
        self.quantities[index_product] -= quantity
        if self.quantities[index_product] <= 0:
            self.remove_product(product)
        else:
            print('Reduced the amount')

    def get_total(self) -> int:
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.get_total(quantity)
        return total


class PaymentValidator:
    def is_valid(self):
        raise NotImplementedError


class PaymentProcessor:
    def purchase(self, cart):
        return cart.get_total()


class CashPaymentValidator(PaymentValidator):
    def is_valid(self):
        return True


class CodeValidator(PaymentValidator):
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        client_code = input('Please, input your code')
        return client_code == self.password


class CashPaymentProcessor(CashPaymentValidator, PaymentProcessor):
    def purchase(self, card):
        if self.is_valid():
            print('Cash payment processing')
            print(f'The total amount of payment is made: {card:.2f}')
        else:
            print('the cart is empty')


class CardPaymentProcessor(CodeValidator, PaymentProcessor):
    def purchase(self, card):
        if self.is_valid():
            print('Card payment processing')
            print('Security code :', self.password)
        else:
            print('wrang code')


if __name__ == '__main__':
    candy = Product("candy", 1059, 0.1, )
    sweet = Product("candy", 1059, 0.1, )
    juice = Product("juice", 3655, 1, )
    cart = ShoppingCart()
    cart.add_product(candy, 0.75)
    cart.add_product(sweet, 0.75)
    cart.add_product(juice, 3)
    print(len(cart))
    print('get_total', ShoppingCart.get_total(cart))
    print(cart[0])
    for cart_item, purchase in zip(cart, ((juice, 3), (candy, 1.5))):
        print('cart_item == purchase', cart_item == purchase)
    cart.remove_product(candy)
    print(len(cart))
    cart.sub_product(juice, 2)
    print(cart[0][1])
    cart.sub_product(juice, 2)
    print(not cart)

