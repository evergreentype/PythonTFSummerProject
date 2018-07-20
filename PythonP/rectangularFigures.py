import funClasses
from funClasses import DEFAULT_NEGATIVE_VALUE

class RectanglePerimeter(funClasses.Perimeter):
	"""Perimeter implementation for a rectangle figure"""

	def __init__(self):
		"""Initialise length (a) and width (b) and add them to properties"""
		super(funClasses.Perimeter, self).__init__()

		self.__a = funClasses.Length()
		self.__b = funClasses.Length()

		self.add_property(self.__a)
		self.add_property(self.__b)

	def assign_properties(self, *args):
		"""Validate and set length (a) and width (b)"""

		if (len(args) == 2):
			# Validate
			if ((self.properties[0].validate_value(args[0]) == False) 
				or (self.properties[1].validate_value(args[1]) == False)):
				return False
			
			# Set properties
			self.properties[0].set_value(args[0])
			self.properties[1].set_value(args[1])

			# Try to calculate a value
			return self.set_value(True, self.calculate_rect_perimeter(self.properties[0], self.properties[1]))
		else:
			return False

	def calculate_rect_perimeter(self, _a, _b):
		"""Standard formula for calculating a rectangle's perimeter"""
		a = _a.get_value()
		b = _b.get_value()

		return 2 * (a + b)


class SquarePerimeter(RectanglePerimeter):
	def __init__(self):
		"""Initialise using the rectangle's class but remove the width (b) property"""
		super(funClasses.Perimeter, self).__init__()
		self.remove_property(self.properties[1])

	def assign_properties(self, *args):
		"""Validate and set length (a)"""

		if (len(args) == 1):
			# Validate
			if (self.properties[0].validate_value(args[0]) == False):
				return False
			
			# Set property
			self.properties[0].set_value(args[0])

			# Try to calculate a value
			return self.set_value(True, self.calculate_rect_perimeter(self.properties[0], self.properties[0]))
		else:
			return False





