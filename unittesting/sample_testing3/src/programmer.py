from person import Person

class Programmer(Person):
    def __init__(self, name, gender, deposit, movielist=[], age=25):
        self.movielist = movielist
        super().__init__(name=name, age=age, gender=gender, deposit=deposit)
    
    def coding(self):
        return "I am coding"