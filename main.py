class Car:
    fuel_type = "Бензин"
    num_wheels = 4
    max_speed = 200

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.current_speed = 0
        self.is_engine_on = False
    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.brand} {self.model}")
    def accelerate(self, speed_increase):
        if self.is_engine_on:
            self.current_speed += speed_increase
            print(f"{self.brand} {self.model}{self.current_speed} ")
        else:
            print(f"{self.brand} {self.model}")
    def stop_engine(self):
        self.is_engine_on = False
        self.current_speed = 0
        print(f"{self.brand} {self.model}")
class Driver:
    license_type = "B"
    max_hours_per_day = 8
    min_driving_age = 18
    def __init__(self, name, age, experience_years):
        self.name = name
        self.age = age
        self.experience_years = experience_years
        self.current_hours_driven = 0
    def drive_car(self, car, hours):
        if self.age >= car.min_driving_age and self.experience_years >= 1:
            if self.current_hours_driven + hours <= self.max_hours_per_day:
                self.current_hours_driven += hours
                print(f"{self.name} {car.brand} {car.model}  {hours} ")
            else:
                print(f"{self.name}")
        else:
            print(f"{self.name} {car.brand} {car.model}")
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)
car3 = Car("Ford", "Mustang", 2020)
driver1 = Driver("John", 25, 3)
driver2 = Driver("Alice", 19, 1)
driver3 = Driver("Bob", 30, 5)
