class Dog:
    species = "Maltese dog"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name}, {self.breed}, says Woof!")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Dora", "Labrador")

print(f"{dog1.name} is a {dog1.species}.")
print(f"{dog2.name} is a {dog2.species}.")

dog1.bark()
dog2.bark()