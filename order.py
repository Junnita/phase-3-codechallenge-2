class Order:
    def __init__(self, customer, coffee, price):
        # Initialize the Order with a Customer instance, a Coffee instance, and a price
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def price(self):
        # Getter for the price property
        return self._price

    @price.setter
    def price(self, value):
        # Setter for the price property with validation
        if getattr (self, '_price'):
            raise AttributeError("Cannot change the price once set")
           
    #This line checks if the _price attribute already exists on the instance (self).
    #If _price is already set, it raises an AttributeError with the message “Cannot change the price once set”.
    #This ensures that the price of the order cannot be changed once it has been initially set.

        if not instance(value, float):
            raise TypeError("Price must be of type float")
            
    #This line checks if the value is not an instance of the float type.
    #If value is not a float, it raises a TypeError with the message “Price must be of type float”.
    #This ensures that only float values can be assigned to the price property.

        if not (1.5 <= value <= 15.0):
            raise ValueError("Price must be between 1.5 and 15.0")
          
    #This line checks if the value is not between 1.5 and 15.0, inclusive.
    #If the value is outside this range, it raises a ValueError with the message “Price must be between 1.0 and 10.0”.
    #This ensures that the price is within a valid range, neither too low nor too high.
 
        self._price = value

    @property
    def customer(self):
        # Getter for the customer property
        return self._customer

    @customer.setter
    def customer(self, value):
        # Setter for the customer property with validation
        if not isinstance(value, Customer):
            raise TypeError("Customer must be of type Customer")
        self._customer = value

    @property
    def coffee(self):
        # Getter for the coffee property
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        # Setter for the coffee property with validation
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be of type Coffee")
        self._coffee = value
        
        
        
        ##Testing order class 
        
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price  # Use _price internally

    @property
    def price(self):
        return self._price
    
# Example usage:
customer = "Junne"
coffee = "Iced coffee"
order = Order(customer, coffee, 9.0)
print(order.price)  # Should print: 5.0
print(customer)
print(coffee)
