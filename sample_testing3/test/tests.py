import coverage
import unittest
from unittest.mock import patch, MagicMock

import sys
sys.path.append('/Users/kraghavan/KarthikaRepo/PycharmProjects/testing/sample_testing3/src')
from confluent_kafka import KafkaException

class TestCelebrity(unittest.TestCase):
    @patch('person.Consumer')
    def setUp(self, mock_consumer):
        mock_consumer.return_value.consumer = MagicMock()
        name = "Tom Cruise"
        ager = 55
        
        from src.celebrity import Celebrity        
        self.celeb=Celebrity(movielist=["Aviator","Ball"],name=name, age=ager, gender='Male')

    @patch('person.Consumer')
    def test_person(self, mock_consumer):
        try:
            # this line below forces the mock consumer magic mock to be assigned to self.celeb.consumer. recommanded step inside test
            # mock_consumer.return_value.consumer = MagicMock()
            # name = "Tom Cruise"
            # ager = 55
            
            # from src.celebrity import Celebrity        
            # self.celeb=Celebrity(movielist=["Aviator","Ball"],name=name, age=ager, gender='Male')
            print(self.celeb)
            assert self.celeb.name == "Tom Cruise"
            assert self.celeb.age == 55
            assert isinstance(mock_consumer, MagicMock)
            assert isinstance(self.celeb.consumer, MagicMock)
            # print("Consumer:",mock_consumer)
            # print(type(mock_consumer))
            # print("Consumer return:",mock_consumer.return_value)
            # print("celeb.consumer:",self.celeb.consumer)

        except KafkaException as exception:
            print("KafkaError ignored")
            pass

if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()

    try:
        unittest.main()
    except:  # catch-all except clause
        pass

    cov.stop()
    cov.save()

    cov.html_report()
    print("Done.")