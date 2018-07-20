import math

DEFAULT_NEGATIVE_VALUE = -1

class MathObject:
	"""Base abstract class inherited by all primitives.

	Implementation of get, set and validate value methods required"""

	value = None

	def set_value(self, *args):
		raise NotImplementedError("Must implement method set_value(self, *args)")

	def get_value(self):
		raise NotImplementedError("Must implement method get_value(self)")

	def validate_value(self, input):
		raise NotImplementedError("Must implement method check_input_value(self, input)")

	def return_value_error(self):
		raise Exception("Value does not exist or does not satisfy the condition")


class Composite:
	"""Base abstract class that identifies composite objects

	Supports adding and removing elements for a list of properties"""

	properties = []

	def add_property(self, val):
		self.properties.append(val)

	def remove_property(self, val):
		"""Remove an element by its value"""
		if val in self.properties:
			self.properties.remove(val)
			return True
		else: return False

	def get_properties(self):
		return self.properties


class CompositeMathObject(Composite, MathObject):
	"""A filler class that combines a primitive (i.e. has a value) and composite (i.e. has properties) types"""

	def set_value(self, flag, *args):
		raise NotImplementedError("Must implement method set_value(self, flag, *args)")


class Length(MathObject):
	"""A simple one-dimentional line"""

	def __init__(self):
		self.value = DEFAULT_NEGATIVE_VALUE

	def set_value(self, *args):
		"""Accepts a single positive value"""

		if (self.validate_value(args[0])):
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

	def validate_value(self, input):
		"""Valida input on existing and having >0 value"""
		if (input != None and input > 0):
			return True
		else:
			return False

class Perimeter(CompositeMathObject, Length):
	"""Inherits properties of a one-dimentional line, but is able to have properties"""
	pass


