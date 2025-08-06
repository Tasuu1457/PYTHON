class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
print("\n_ _ _ Animal Type _ _ _")
animal_type = Animal("Leo", "Lion")
animal_type.display()

print("\n_ _ _ Dog Type _ _ _")
dog_type = Dog("Dora", "American Eskimo Dog")
dog_type.display()