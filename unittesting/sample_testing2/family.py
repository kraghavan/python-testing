from supportresource import SupportResource

class Parent:

    def __init__(self):
        print("In the Parent constructor.")
        self.supportresource = SupportResource()

    def foo(self):
        print("Parent's foo")
        print(self.supportresource.use_resource())

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("In the Child constructor")
    
    def foo(self):
        print("Child's foo")
        super().foo()