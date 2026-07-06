class Burger:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False

    def __str__(self):
        return f"Burger Size: {self.size} | Cheese: {self.cheese} | Pepperoni: {self.pepperoni}"


class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def set_size(self, size: str):
        self.burger.size = size
        return self  

    def add_cheese(self):
        self.burger.cheese = True
        return self

    def add_pepperoni(self):
        self.burger.pepperoni = True
        return self

    def build(self) -> Burger:
        return self.burger


my_order = (
    BurgerBuilder()
    .set_size("Large")
    .add_cheese()
    .add_pepperoni()
    .build()
)

print(my_order)
