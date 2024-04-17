from socialMedia import SocialMedia
from confluent_kafka import Consumer

import threading

class Person(threading.Thread):
    def __init__(self, name, age=25, gender='Female'):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender
        f"Person {self.name} created."
        self.consumer = Consumer({
            'bootstrap.servers': 'test',
            'group.id': 'mygroup',
            'auto.offset.reset': 'earliest'
            })
        self.consumer.subscribe(['mytopic'])
    def __str__(self):
        return f"{self.name} is {self.age} years old and is a {self.gender}"
