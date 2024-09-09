class Customer:
    def __init__(self, name):
        # Initialize the Customer with a name
        self.name = name  # This will call the setter method

    @property
    def name(self):
        # Getter for the name property
        return self._name

    @name.setter
    def name(self, value):
        # Setter for the name property with validation
        if not isinstance(value, str):  # Fix: Use isinstance() instead of instance()
            raise TypeError("Name must be of type str")
        
    #This line checks if the value is not an instance of the str (string) type.
    #If value is not a string, it raises a TypeError with the message “Name must be of type str”.
    #This ensures that only string values can be assigned to the name property.

           
        if not (1 <= len(value) <= 20):
            raise ValueError("Name must be between 1 and 20 characters")
        
     
    #This line checks if the length of the value is not between 1 and 15 characters, inclusive.
    #If the length of value is outside this range, it raises a ValueError with the message “Name must be between 1 and 15 characters”.
    #This ensures that the name is neither too short (less than 1 character) nor too long (more than 15 characters).
   

        self._name = value  # This is correct

       ## Testing customer class 
try:
    customer1 = Customer("Junne")
    customer2 =Customer("Gladys")
    print(f"Customer 1: {customer1.name}")  # Expected: Junne
    print(f"Customer 2: {customer2.name}")
except Exception as e:   #
    print(f"Error: {e}")  #If an exception is raised, this line will print the error message.
    
    