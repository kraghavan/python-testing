from unittest.mock import MagicMock
from confluent_kafka import Consumer

class MockLiving(MagicMock):
    def __init__(self):
        super(MockLiving).__init__()
        f"Entered Mock living Class Constructor"

    # def get_description(self):
    #     return f"{self.year} {self.make} {self.model}"

class MockConsumer(MagicMock):
    pass