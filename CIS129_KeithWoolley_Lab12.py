# Lab 12 (Class)
# Keith Woolley
# 11/25/2024
# Pet class that allows the creation of a pet object and a main method that allows the user to input information to create a pet object.
# Prints the information of the created pet object after.

# The Pet class
class Pet:
    """Pet class to create a pet"""

    def __init__(self, name, type, age):
        """Initialize a pet object"""
        if not isinstance(age, int):
            raise TypeError('Age must be an integer')

        if age < 0:
            raise ValueError('Age must be positive')
        
        self.name = name
        self.type = type
        self.age = age

    def setName(self, name):
        """Set the pet's name"""
        self.name = name

    def setType(self, type):
        """Set the pet's type"""
        self.type = type

    def setAge(self, age):
        """Set the pet's age"""
        if not isinstance(age, int):
            raise TypeError('Age must be an integer')

        if age < 0:
            raise ValueError('Age must be positive')
        
        self.age = age

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age
    
# Main method that creates the pet object and displays its information
def main():
    # Initialize variables
    name_input = ''
    type_input = ''
    age_input = 0

    # Create pet object
    pet = Pet(name_input, type_input, age_input)

    # Set the pet's name from input
    name_input = input('Enter pet name')
    pet.setName(name_input)

    # Set the pet's type from input
    type_input = input('Enter pet type')
    pet.setType(type_input)

    # Set the pet's age from input
    while True:
        try:
            age_input = int(input('Enter pet age'))
            if age_input < 0:
                print('Age must be positive')
            else:
                pet.setAge(age_input)
                break
        except ValueError:
            print('Value must be an integer')
    
    # Display the pet's name, type, and age
    print(f'Your pet name: {pet.getName()}')
    print(f'Your pet type: {pet.getType()}')
    print(f'Your pet age: {pet.getAge()}')

main()







    