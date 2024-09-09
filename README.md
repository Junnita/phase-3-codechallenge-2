# Coffee Shop 
- This project implements a simple coffee shop management system with three main classes: Customer, Coffee, and Order. The system allows for creating customers, coffees, and orders, and provides various methods to manage and retrieve information about them.
Classes and Methods
Customer
__init__(self, name)

    - Initializes a Customer instance with a name.
    Parameters:
        name (str): The name of the customer. Must be between 1 and 15 characters, inclusive.

### Name (property)

    Returns the customer’s name.
        Type: str
    Constraints:
        Must be between 1 and 15 characters, inclusive.
        Can be changed after the customer is instantiated.

### Orders()

    Returns a list of all orders for that customer.
    Returns: List of Order instances.

### Coffees()

    Returns a unique list of all coffees a customer has ordered.
    Returns: List of Coffee instances.

 - create_order(coffee, price)

    Creates and returns a new Order instance and associates it with the customer and the provided coffee object.
    Parameters:
        coffee (Coffee): The coffee object.
        price (float): The price of the order.
            Returns: Order instance.

 ### Most_aficionado(coffee) (classmethod)

    Returns the Customer instance that has spent the most money on the provided coffee instance.
    Parameters:
        coffee (Coffee): The coffee object.
    Returns: Customer instance or None if there are no customers for the coffee.

### Coffee
__init__(self, name)

    Initializes a Coffee instance with a name.
    Parameters:
        name (str): The name of the coffee. Must be at least 3 characters long.
### Name (property)

    Returns the coffee’s name.
    Type: str
    Constraints:
        Must be at least 3 characters long.
                Cannot be changed after the coffee is instantiated.

### Orders()

    Returns a list of all orders for that coffee.
    Returns: List of Order instances.

### Customers()

    Returns a unique list of all customers who have ordered a particular coffee.
    Returns: List of Customer instances.

### Num_orders()

    Returns the total number of times a coffee has been ordered.
    Returns: int

### Average_price()

    Returns the average price for a coffee based on its orders.
    Returns: float

### Order
__init__(self, customer, coffee, price)

    Initializes an Order instance with a Customer instance, a Coffee instance, and a price.
    Parameters:
        customer (Customer): The customer object.
        coffee (Coffee): The coffee object.
        price (float): The price of the order. Must be between 1.0 and 10.0, inclusive.

### Price (property)

    Returns the price for the order.
    Type: float
    Constraints:
        Must be between 1.0 and 10.0, inclusive.
        Cannot be changed after the order is instantiated.

### Customer (property)

    Returns the customer object for that order.
    Type: Customer
    coffee (property)

    Returns the coffee object for that order.
    Type: Coffee

# Usage

To use this system, create instances of Customer, Coffee, and Order classes and call the methods as needed. Below is an example of how to use the classes:
# Example usage
- customer1 = Customer("Junne")
- coffee1 = Coffee("Iced coffee")
- order1 = customer1.create_order(coffee1, 9.0)

******

- print(customer1.name)  # Output: Junne
- print(coffee1.name)    # Output: Iced coffee 
- print(order1.price)    # Output: 9.0
- print(order1.customer) # Output: <Customer instance>
- print(order1.coffee)   # Output: <Coffee instance>

# License

- This project is licensed under the MIT License.

Feel free to customize this README file further to suit your project’s needs! If you have any questions or need more details, let me know.

# Author

**JUNNE WANJA**




        

