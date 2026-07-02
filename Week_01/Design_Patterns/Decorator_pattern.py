def base_coffee():
    return "Simple Coffee", 2.00

def with_milk(coffee_func):
    def wrapper():
        desc, price = coffee_func()
        return f"{desc} + Milk", price + 0.50
    return wrapper

def with_sugar(coffee_func):
    def wrapper():
        desc, price = coffee_func()
        return f"{desc} + Sugar", price + 0.25
    return wrapper

fancy_coffee = with_sugar(with_milk(base_coffee))

description, total_cost = fancy_coffee()
print(f"Order: {description} | Total: ${total_cost:.2f}")
# Output: Order: Simple Coffee + Milk + Sugar 