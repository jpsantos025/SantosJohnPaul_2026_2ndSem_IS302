class Vehicle:
    def __init__(self, jps_car_brand, jps_car_model):
        self.jps_car_brand = jps_car_brand
        self.jps_car_model = jps_car_model


class Car(Vehicle):
    def __init__(self, jps_car_brand, jps_car_model, jps_release_year):
        super().__init__(jps_car_brand, jps_car_model)
        self.jps_release_year = jps_release_year

    def display_car(self):
        print(self.jps_car_brand, self.jps_car_model, self.jps_release_year)


# example usage
jps_car1 = Car("BMW", "X5", 2020)
jps_car1.display_car()

#JohnPaulSantos