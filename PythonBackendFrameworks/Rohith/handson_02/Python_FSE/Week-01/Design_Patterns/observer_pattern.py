from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def notify(self, product_name: str) -> None:
        pass


class ProductLaunchNotifier(ABC):
    """The Subject interface defining subscription management."""
    @abstractmethod
    def subscribe(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def notify_customers(self, product_name: str) -> None:
        pass


class AmazonUser(Customer):
    def __init__(self, name: str):
        self.name = name

    def notify(self, product_name: str):
        print(f"Dear {self.name}, the product '{product_name}' is now available.")


class IPhoneLaunchNotifier(ProductLaunchNotifier):
    def __init__(self):
        self.customers = []  

    def subscribe(self, customer: Customer) -> None:
        self.customers.append(customer)

    def unsubscribe(self, customer: Customer) -> None:
        self.customers.remove(customer)

    def notify_customers(self, product_name: str) -> None:
        for customer in self.customers:
            customer.notify(product_name)


def main():
    notifier = IPhoneLaunchNotifier()
    
    user1 = AmazonUser("Alice")
    user2 = AmazonUser("Bob")

    notifier.subscribe(user1)
    notifier.subscribe(user2)

    
    notifier.notify_customers("iPhone 15")


if __name__ == "__main__":
    main()