import coverage
import unittest
from unittest.mock import patch, MagicMock

import sys
sys.path.append('/Users/kraghavan/KarthikaRepo/PycharmProjects/testing/sample_testing3/src')
from confluent_kafka import KafkaException

class TestCelebrity(unittest.TestCase):
    # @patch('person.Consumer')
    # def setUp(self, mock_consumer):
    #     mock_consumer.return_value.consumer = MagicMock()
    #     name = "Tom Cruise"
    #     ager = 55
        
    #     from src.celebrity import Celebrity        
    #     self.celeb=Celebrity(movielist=["Aviator","Ball"],name=name, age=ager, gender='Male')


    @patch('person.Consumer')
    @patch('person.ssl.create_default_context')
    @patch('person.pika.SSLOptions')
    @patch('person.pika.ConnectionParameters')
    def test_person(self, mock_connection_parameters,mock_pika_ssloptions,mock_ssl_create_default_context, mock_consumer):
        try:
            # this line below forces the mock consumer magic mock to be assigned to self.celeb.consumer. recommanded step inside test
            mock_connection_parameters.return_value = "mock_connection_parameters"
            mock_pika_ssloptions.return_value = "mock_pika_ssloptions_return_value"
            mock_ssl_create_default_context.return_value = "mock_ssl_create_default_context_return_value"
            mock_consumer.return_value.consumer = MagicMock()
            mock_consumer.return_value.subscribe = MagicMock()
            name = "Karthika"
            ager = 35
            
            from src.programmer import Programmer        
            self.celeb=Programmer(movielist=["Aviator","Ball"],name=name, age=ager, gender='FeMale', deposit=1000)
            print(self.celeb)
            assert self.celeb.name == "Karthika"
            assert self.celeb.age == 35
            assert isinstance(mock_consumer, MagicMock)
            assert isinstance(self.celeb.consumer, MagicMock)
            assert self.celeb.consumer == mock_consumer.return_value
            mock_consumer.assert_called_once()
            mock_ssl_create_default_context.assert_called_once()
            mock_ssl_create_default_context.assert_called_once_with(cafile="ca_certificate.pem")
            mock_connection_parameters.assert_called_once()
            assert self.celeb.investment_decade() == 2000.0

            print("Consumer:",mock_consumer)
            print("Consumer return:",mock_consumer.return_value)
            print("celeb.consumer:", self.celeb.consumer)
            print("mock sec context:", mock_ssl_create_default_context)
            print("mock_pika_ssloptions:", mock_pika_ssloptions)

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