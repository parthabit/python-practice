class Car:
    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.speed = 0
        self.engine_on = False

    def start_engine(self):
        if self.fuel > 0:
            self.engine_on = True
            print(f"{self.brand} {self.model} engine started.")
        else:
            print("No fuel! Cannot start the engine.")

    def stop_engine(self):
        self.engine_on = False
        self.speed = 0
        print("Engine stopped.")

    def accelerate(self, increase):
        if self.engine_on:
            if self.fuel > 0:
                self.speed += increase
                self.fuel -= 1
                print(f"Speed increased to {self.speed} km/h")
                print(f"Fuel left: {self.fuel} liters")
            else:
                print("Out of fuel!")
        else:
            print("Start the engine first!")

    def brake(self, decrease):
        if self.speed > 0:
            self.speed -= decrease
            if self.speed < 0:
                self.speed = 0
            print(f"Speed reduced to {self.speed} km/h")
        else:
            print("Car is already stopped.")

    def show_status(self):
        print("\n--- Car Status ---")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Speed: {self.speed} km/h")
        print(f"Fuel: {self.fuel} liters")
        print(f"Engine On: {self.engine_on}")
        print("------------------\n")


# Create car object
my_car = Car("Toyota", "Fortuner", 5)

# Use the car
my_car.start_engine()
my_car.accelerate(20)
my_car.accelerate(30)
my_car.brake(10)
my_car.show_status()
my_car.stop_engine()
