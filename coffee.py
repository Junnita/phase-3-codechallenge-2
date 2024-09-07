class Coffee:
    def __init__(self, name):
        # Initialize the Coffee with a name
        self._name = name

    @property
    def name(self):
        # Getter for the name property
        return self._name

    @name.setter
    def name(self, value):
        # Setter for the name property with validation
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the name of the coffee once set")
           
    #This line checks if the _name attribute already exists on the instance (self).
    #If _name is already set, it raises an AttributeError with the message “Cannot change the name of the coffee once set”.
    #This ensures that the name of the coffee cannot be changed once it has been initially set.
  
        if not  instance(value, str):
            raise TypeError("Name must be of type str")
         
     #This line checks if the value is not an instance of the str (string) type.
     #If value is not a string, it raises a TypeError with the message “Name must be of type str”.
     #This ensures that only string values can be assigned to the name property.
   
        if len(value) < 3:
            raise ValueError("Name length must be greater or equal to 3 characters")
        
    #This line checks if the length of the value is less than 3 characters.
    #If the length of value is less than 3, it raises a ValueError with the message “Name length must be greater or equal to 3 characters”.
    #This ensures that the name is not too short and has at least 3 characters.
  
        self._name = value
