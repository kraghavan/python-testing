class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades  # grades is a dictionary with subject as key and grade as value

    def get_grade(self, subject):
        return self.grades.get(subject, "Subject not found")

    def get_average_grade(self):
        return sum(self.grades.values()) / len(self.grades)