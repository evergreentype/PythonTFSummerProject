import math

class MathObject:
	"""Base abstract class inherited by all primitives.

	Implementation of get and set value methods required"""

	value = None

	def set_value(self, *args):
		raise NotImplementedError("Must implement method set_value()")

	def get_value(self):
		raise NotImplementedError("Must implement method get_value()")

	def return_value_error(self):
		raise Exception("Value does not exist or does not satisfy the condition")


class Composite:
	"""Base abstract class that identifies composite objects

	Supports adding and removing elements for a list of properties """

	properties = []

	def add_property(self, arg):
		self.properties.append(arg)

	def get_properties(self):
		return self.properties


class CompositeMathObject(MathObject, Composite):
	"""A filler class that combines a primitive (i.e. has a value) and composite (i.e. has properties) types"""
	pass


class Length(MathObject):
	"""A simple one-dimentional line"""

	def __init__(self):
		self.value = -1

	def set_value(self, *args):
		"""Accepts a single positive value"""
		if (len(args) == 1 and args[0] > 0):
			self.value = float(args[0])
			return True
		else:
			# raise Exception("Wrong amount of args or value < 0")
			return False

	def get_value(self):
		"""Returns a single positive value or a negative -1, if value is not set"""
		if (self.value != None and self.value > 0):
			return self.value
		else:
			return self.value


class Perimeter(Length, CompositeMathObject):
	"""Inherits properties of a one-dimentional line, but is able to have properties"""
	pass


