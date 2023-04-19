class Product:
    name: str = 'name'
    price: int = 0
    unit: float = 0.1

    def get_total(self, unit_product=unit) -> int:
        total_price: float = self.price * unit_product / self.unit
        return int(total_price)


product1 = Product()
product1.name = 'apple'
product1.price = 1059
product1.unit = 0.1
print(product1.get_total(0.7))
print(product1.get_total())
