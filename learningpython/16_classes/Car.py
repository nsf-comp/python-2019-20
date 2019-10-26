class Car:

    def __init__(self, name, brand, speed):
        self.name = name
        self.brand = brand
        self.speed = speed


    def drive(self):
        print(self.name + ' car driving at ' + str(self.speed) + ' miles/hr')

    def myCarModel(self):
        print(self.name + " " + self.brand)



camryCar = Car('Camry', 'Toyota' , 150)

bmwCar = Car('X5', 'BMW', 200)


#bmwCar.myCarModel();