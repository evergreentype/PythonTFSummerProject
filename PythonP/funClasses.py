import math

# Global constant for initial value initialisation for positive primitives
DEFAULT_NEGATIVE_VALUE = -1
DEFAULT_NAME = "default name"
DEFAULT_UNITS = {1:"units", 2:"units squared"}

class MathObject:
	"""Base abstract class inherited by all primitives.

	Implementation of get-, set- and validate-value methods required; init method must set values to defaults. It is not supposed to be initialised directly"""

	# Digital value
	value = None
	# Name (string)
	__name = None
	# Unit (string)
	__unit = None

	def __init__(self):
		raise NotImplementedError("Must implement method init(self)")

	# Implementation methods for value operations
	def set_value(self, *args):
		raise NotImplementedError("Must implement method set_value(self, *args)")
	def get_value(self):
		raise NotImplementedError("Must implement method get_value(self)")
	def validate_value(self, input):
		raise NotImplementedError("Must implement method validate_value(self, input)")

	# Built-in methods for name
	def set_name(self, xName):
		self.__name = xName
	def get_name(self):
		return self.__name

	# Built-in methods for unit
	def set_unit(self, xUnit):
		self.__unit = xUnit
	def get_unit(self):
		return self.__unit


class Composite:
	"""Base abstract class that identifies composite objects (objects with properties of primitives).

	Supports adding and removing elements for the list of properties. It is not supposed to be initialised directly"""

	properties = []

	def add_property(self, val):
		self.properties.append(val)

	def remove_property(self, val):
		"""Remove an element by its value, returns if it was successful"""
		if val in self.properties:
			self.properties.remove(val)
			return True
		else: 
			return False

	def get_properties(self):
		return self.properties


class CompositeMathObject(Composite, MathObject):
	"""Base abstract class that combines a primitive (i.e. has a value) and composite (i.e. has properties) types.

	It is not supposed to be initialised directly"""

	def set_value(self, flag, val, *args):
		"""Set the flag = 1 to set the value. Class-specific validation included
		Set the flag = 0 to invoke the method that assign properties. Implementation is class specific"""

		# Try to assign a value to itself
		if (flag == True):
			if (((val != None) and (self.validate_value(val))) == True):
				self.value = val
				return True
			else:
				return False
		# Insert the value of val into args and pass it into the assigning method
		elif (flag == False):
			temp = list(args)
			temp.insert(0, val)
			args = tuple(temp)
			return self.assign_properties(*args)

	def assign_properties(self, *args):
		raise NotImplementedError("Must implement method assign_properties(self, *args)")


class Length(MathObject):
	"""1D primitive"""

	def __init__(self):
		self.value = DEFAULT_NEGATIVE_VALUE
		self.set_name(DEFAULT_NAME)
		self.set_unit(DEFAULT_UNITS[1])

	def set_value(self, *args):
		"""Accepts a single positive value"""

		if (self.validate_value(args[0])):
			self.value = float(args[0])
			return True
		else:
			return False

	def get_value(self):
		"""Returns a single positive value or a negative -1, if value is not set"""
		if (self.value != None and self.value > 0):
			return self.value
		else:
			return DEFAULT_NEGATIVE_VALUE

	def validate_value(self, input):
		"""Validate if input exists and has > 0 value"""
		if (input != None and input > 0):
			return True
		else:
			return False


class Perimeter(CompositeMathObject, Length):
	"""Inherits properties of a one-dimentional line, but is able to have properties"""
	pass


class Area(CompositeMathObject, Length):
	"""Abstract 2D concept"""

	def __init__(self):
		self.value = DEFAULT_NEGATIVE_VALUE
		self.set_name(DEFAULT_NAME)
		self.set_unit(DEFAULT_UNITS[2])



