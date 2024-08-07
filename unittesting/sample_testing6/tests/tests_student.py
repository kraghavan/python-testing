import unittest
from hypothesis import given, strategies as st
from src.student import Student  # Assuming your Student class is in student.py

class TestStudent(unittest.TestCase):

    @given(
        name=st.text(),
        age=st.integers(min_value=18, max_value=100),
        grades=st.dictionaries(keys=st.text(min_size=1), values=st.floats(min_value=0, max_value=100), min_size=5, max_size=5)
    )
    def test_get_average_grade(self, name, age, grades):
        student = Student(name, age, grades)
        expected_average = sum(grades.values()) / len(grades)
        self.assertAlmostEqual(student.get_average_grade(), expected_average, places=2)

if __name__ == "__main__":
    unittest.main()