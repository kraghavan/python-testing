from socialMedia import SocialMedia
from confluent_kafka import Consumer
import pika
import ssl
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
        self.context = ssl.create_default_context(cafile="ca_certificate.pem")
        self.ssl_options = pika.SSLOptions(self.context, "localhost")
        self.conn_params = pika.ConnectionParameters(port=5671,
                                        ssl_options=self.ssl_options)

    def __str__(self):
        return f"{self.name} is {self.age} years old and is a {self.gender}"
