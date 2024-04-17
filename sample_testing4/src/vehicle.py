import threading
from livingThings import Pet
from livingThings import Person
from confluent_kafka import Consumer

class Vehicle(threading.Thread):
    def __init__(self, make, color='white'):
        self.make = make
        self.color = color
        self.tyres = 4
        self.driver = Person('Hermione', 30, 'Female')
        self.consumer = Consumer({
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'mygroup',
            'auto.offset.reset': 'earliest'
        })

        print(f"Vehicle of color {self.color} with {self.tyres} tyres was created. The driver is {self.driver.name}")
        super().__init__()
    
    def get_description(self):
        return f"{self.make} {self.color}"

    def start(self):
        return f"Vehicle of color {self.color} started by turning on keys in ignition" 

    # def evaluate_passenger(self, passenger): # mock up this guy in your unittest to actually use a mock class
    #     if passenger == 'H':
    #         self.copassenger = Person('Harry', 30, "Male")
    #     else:
    #         self.copassenger = Pet('Rover', 'dog')