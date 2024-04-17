class SupportResource:

    def __init__(self):
        print("Expensive network call")

    def use_resource(self) -> str:
        print("Another expensive network call")
        return "bar"