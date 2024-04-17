from car import Car


class ElectricCar(Car):
    def __init__(self, make, color='white', doors=4, battery_size=75):
        super(ElectricCar,self).__init__(make, color, doors)
        self.battery_size = battery_size
        print(f"Electric car of color {self.color} with {self.doors} doors and a {self.battery_size} kWh battery was created. The driver is {self.driver.name}")

    def get_description(self):
        return f"{self.make} {self.color} with {self.doors} doors and a {self.battery_size} kWh battery"
    
    def start(self):
        return f"Electric car of color {self.color} started by pressing the start button"
    