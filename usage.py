class Customer:
    def __init__(self, name):
        self.name = name

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    def __str__(self):
        return self.name


class Coffee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    def __str__(self):
        return f"Order for {self.customer} - {self.coffee} (${self.price})"


# Example usage
customer1 = Customer("Junne")
coffee1 = Coffee("Iced coffee")
order1 = customer1.create_order(coffee1, 9.0)

print(customer1.name)  # Output: Junne
print(coffee1.name)    # Output: Iced coffee 
print(order1.price)    # Output: 9.0
print(order1.customer) # Output: Junne
print(order1.coffee)   # Output: Latte
print(order1)          # Output: Order for Junne - Iced coffee ($9.0)