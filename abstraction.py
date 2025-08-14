from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def info(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
    def info(self):
        return f"Dog - Name: {self.name}, Age: {self.age}"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
    def info(self):
        return f"Cat - Name: {self.name}, Age: {self.age}"
    
class Bird(Animal):
    def speak(self):
        return "Tweet!"
    
    def info(self):
        return f"Bird - Name: {self.name}, Age: {self.age}"
    
class AnimalManager:
    def __init__(self):
        self.animals = []
        
    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        
    def show_all_animals(self):
        if not self.animals:
            print("No animals found in the system.")
        else:
            for animal in self.animals:
                print(animal.info(), "| Sound: ", animal.speak())
                
if __name__ == "__main__":
    manager= AnimalManager()
    
    manager.add_animal(Dog("Buddy", 5))
    manager.add_animal(Cat("Tokyo", 3))
    manager.add_animal(Bird("Sweety", 2))
    
    manager.show_all_animals()