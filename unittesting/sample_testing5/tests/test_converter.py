import unittest
from hypothesis import given, strategies as st
from src.converter import Converter

class TestConverter(unittest.TestCase):

    @given(st.text())
    def test_str_to_ascii_to_str(self, input_str):
        # Convert string to ASCII and back
        ascii_list = Converter.str_to_ascii(input_str)
        result_str = Converter.ascii_to_str(ascii_list)
        # Check if the round-trip conversion yields the original string
        self.assertEqual(input_str, result_str)

    @given(st.lists(st.integers(min_value=0, max_value=127)))
    def test_ascii_to_str_to_ascii(self, ascii_list):
        # Convert ASCII list to string and back
        str_value = Converter.ascii_to_str(ascii_list)
        result_ascii_list = Converter.str_to_ascii(str_value)
        # Check if the round-trip conversion yields the original ASCII list
        self.assertEqual(ascii_list, result_ascii_list)

if __name__ == "__main__":
    unittest.main()