from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, name, model):
        self.name = name
        self.model = model
        
    @abstractmethod
    def get_details(self):
        pass
    
class BMW(Car):
    def get_details(self):
        return f"BMW {self.model}: German engineering, luxury performance."

class Ferrari(Car):
    def get_details(self):
        return f"Ferrari {self.model}: Italian passion, exhilarating speed."
    
class CarManagement:
    def __init__(self):
        self.car = []
        
    def add_car(self, car: Car):
        self.car.append(car)
        
    def show_all_cars(self):
        if not self.car:
            print("No cars found in the system.")
        else:
            for car in self.car:
                print(car.get_details())

if __name__ == "__main__":
    manager = CarManagement()
    
    manager.add_car(BMW("G70 series", 7))
    manager.add_car(Ferrari("12Cilindri", 12))

    manager.show_all_cars()