class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def calculate_fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_charge = base_fare * 5
        total_fare = base_fare + maintenance_charge
        return total_fare


school_bus = Bus("BRTC Bus", 50)
print(f"Total Bus fare for {school_bus.name} with capacity {school_bus.capacity}: ${school_bus.calculate_fare():.2f}")

car = Vehicle("Premio", 4)
print(f"Total vehicle fare for {car.name} with capacity {car.capacity}: ${car.calculate_fare():.2f}")