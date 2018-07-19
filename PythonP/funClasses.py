import math

class MathObject():
    def __init__(self):
        raise NotImplementedError("Must implement method find_value()")

    def find_value(self, *args):
        raise NotImplementedError("Must implement method find_value()")

class Length(MathObject):
	def __init__(self):
		self.__value = -1

	def find_value(self, *args):
		if (len(args) == 1 and args[0] > 0):
			return float(args[0])
		else:
			raise Exception("Wrong amount of args or value < 0")