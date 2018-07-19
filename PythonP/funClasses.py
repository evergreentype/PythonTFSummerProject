import math

class MathObject:
	"""Base abstract class inherited by all primitives"""

	value = None

	def set_value(self, *args):
		raise NotImplementedError("Must implement method set_value()")

	def get_value(self):
		raise NotImplementedError("Must implement method get_value()")

	def return_value_error(self):
		raise Exception("Value does not exist or does not satisfy the condition")


class Composite:
	"""Base abstract class that identifies composite objects"""

	properties = []

	def add_property(self, arg):
		self.properties.append(arg)

	def get_properties(self):
		return self.properties


class CompositeMathObject(MathObject, Composite):
	pass


class Length(MathObject):
	"""A simple one-dimentional line"""

	def __init__(self):
		self.value = -1

	def set_value(self, *args):
		if (len(args) == 1 and args[0] > 0):
			self.value = float(args[0])
			return True
		else:
			# raise Exception("Wrong amount of args or value < 0")
			return False

	def get_value(self):
		if (self.value != None and self.value > 0):
			return self.value
		else:
			return self.value


class Perimeter(Length, CompositeMathObject):
	pass


