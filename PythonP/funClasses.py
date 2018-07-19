import math

class MathObject():
	"""Base class inherited by all math objects"""

	def __init__(self):
		self.valsAmount = 0
		raise NotImplementedError("Must implement method init()")

	def find_value(self, *args):
		raise NotImplementedError("Must implement method find_value()")


class Length(MathObject):
	"""A simple one-dimentional line"""

	def __init__(self):
		self.__value = -1
		self.valsAmount = 0

	def find_value(self, *args):
		if (len(args) == 1 and args[0] > 0):
			return float(args[0])
		else:
			raise Exception("Wrong amount of args or value < 0")
