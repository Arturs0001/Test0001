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

class Driver:
    license_type = "B"
    max_hours_per_day = 8
    min_driving_age = 18
    def __init__(self, name, age, experience_years):
        self.name = name
        self.age = age
        self.experience_years = experience_years
        self.current_hours_driven = 0
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)
car3 = Car("Ford", "Mustang", 2020)
driver1 = Driver("John", 25, 3)
driver2 = Driver("Alice", 19, 1)
driver3 = Driver("Bob", 30, 5)
