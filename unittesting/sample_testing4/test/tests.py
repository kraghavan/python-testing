import unittest
from unittest.mock import patch

from test.mockClass import MockConsumer

import sys
sys.path.append('/Users/kraghavan/KarthikaRepo/PycharmProjects/testing/src')
from src.electricCar import ElectricCar

#Person = unittest.mock.MagicMock()

class TestElectricCar(unittest.TestCase):
    #with patch('src.livingThings.Person', MockLiving):
    # @patch('src.livingThings.Person')
    # def setUp(self, MockLiving):
    #     self.make = 'Tesla'
    #     self.color = 'red'
    #     self.ecar = ElectricCar(self.make, self.color)
    #     f"print ecar driver: {self.ecar.driver}"
    #     f"Mocked address: {MockLiving}"

    # def test_get_description(self):
    #     expected_description = f"{self.make} {self.color} with {self.doors} doors and a {self.battery_size} kWh battery"
    #     self.assertEqual(self.ecar.get_description(), expected_description)

    @patch('confluent_kafka.Consumer', autospec=True)
    def test_start(self, mockLiving):
        self.make = 'Tesla'
        self.color = 'red'
        self.ecar = ElectricCar(self.make, self.color)
        expected_start = f"Electric car of color {self.color} started by pressing the start button"
        self.assertEqual(self.ecar.start(), expected_start)
        print("mockLiving:{}".format(type(mockLiving)))
        mockLiving.assert_called_once()
        #self.assertEqual(type(self.ecar.driver), MockLiving)

    # def test_stop(self):
    #     expected_stop = f"Car of color {self.color} stopped by turning not filling fuel"
    #     self.assertEqual(self.car.stop(), expected_stop)

    # @patch.object(Car, 'stop')
    # def teststop(self):
    #     return f"Car of color {self.color} stopped by turning not filling fuel"

if __name__ == '__main__':
    unittest.main()