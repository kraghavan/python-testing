from person import Person

class Celebrity(Person):
    def __init__(self, name, gender,movielist=[], age=25):
        self.movielist = movielist
        super().__init__(name=name, age=age, gender=gender)