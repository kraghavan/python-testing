class Person():
    def __init__(self, name, age=25, gender='Female'):
        self.name = name
        self.age = age
        self.gender = gender
        f"Person {self.name} created."

    def __str__(self):
        return f"{self.name} is {self.age} years old and is a {self.gender}"


class Pet:
    def __init__(self, name, type='dog'):
        self.name = name
        self.type = type

    def speak(self):
        return f"My pet is a {self.type} and its name is {self.name} "