class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def display_all():
        print(new_car.price)
        print(new_car.speed)
        print(new_car.fuel)
        print(new_car.mileage)        


new_car1 = Car(100000, "100 MPH", "Full", 10000)
new_car2 = Car(200000, "200 MPH", "Empty", 20000)
new_car3 = Car(300000, "300 MPH", "Full", 30000)
new_car4 = Car(400000, "400 MPH", "Empty", 40000)


print(new_car4.fuel)