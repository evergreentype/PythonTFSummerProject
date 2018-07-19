import math

class MathObject():
    def __init__(self):
        pass

    def find_value(self, *args):
        raise NotImplementedError("Must implement method find_value()")

class Length(MathObject):
    def find_value(self, *args):
        if (len(args) == 1):
            return float(args[0])
        else:
            raise Exception("Wrong amount of args")

myval = Length()

print(myval.find_value(1))