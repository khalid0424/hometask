class Car:

    total_cars = 0

    def __init__(self, model):
        self.model = model
        Car.total_cars += 1  
    
    def total_car_count(cls):
        return cls.total_cars


car1 = Car("Toyota")
car2 = Car("BMW")
car3 = Car("Honda")


print(Car.total_car_count())  
