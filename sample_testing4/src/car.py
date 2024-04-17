from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, color='white', doors=4):
        super(Car, self).__init__(make, color)
        self.doors = doors
        print(f"Car of color {self.color} with {self.doors} doors was created. The driver is {self.driver.name}")

    def get_description(self):
        return f"{self.make} {self.color} with {self.doors} doors"
    
    def stop(self):
        return f"Car of color {self.color} stopped by turning off keys in ignition"
