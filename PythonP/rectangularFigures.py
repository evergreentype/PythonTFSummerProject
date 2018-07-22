import funClasses
from funClasses import DEFAULT_NEGATIVE_VALUE, DEFAULT_NAME


# CLASSES
class RectanglePerimeter(funClasses.Perimeter):
	"""Perimeter implementation for a rectangle figure"""

	def __init__(self):
		"""Initialise length and width and add them to get_properties()"""
		super(RectanglePerimeter, self).__init__()

		# Set defaults
		self.set_name("Perimeter of Rectangle")

		# Initialise get_properties()
		__l = funClasses.Length()
		__w = funClasses.Length()
		__l.set_name("Length")
		__w.set_name("Width")

		# Add to get_properties()
		self.add_property(__l)
		self.add_property(__w)

	def try_set_value(self, *args):
		# Try to calculate a value
		return self.set_value(self.calculate_rect_perimeter(self.get_properties()[0], self.get_properties()[1]))

	def calculate_rect_perimeter(self, _l, _w):
		"""Standard formula for calculating a rectangle's perimeter"""
		l = _l.get_value()
		w = _w.get_value()

		return 2 * (l + w)


class RectangleArea(funClasses.Area):
	def __init__(self):
		"""Initialise length and width and add them to get_properties()"""
		super(RectangleArea, self).__init__()

		# Set defaults
		self.set_name("Area of Rectangle")

		# Initialise get_properties()
		__l = funClasses.Length()
		__w = funClasses.Length()
		__l.set_name("Length")
		__w.set_name("Width")

		# Add to get_properties()
		self.add_property(__l)
		self.add_property(__w)

	def try_set_value(self, *args):
		# Try to calculate a value
		return self.set_value(self.calculate_rect_area(self.get_properties()[0], self.get_properties()[1]))

	def calculate_rect_area(self, _l, _w):
		"""Standard formula for calculating a rectangle's area"""
		l = _l.get_value()
		w = _w.get_value()

		return l * w

class SquarePerimeter(RectanglePerimeter):
	def __init__(self):
		"""Initialise using the rectangle's class but remove the width (b) property"""
		super(SquarePerimeter, self).__init__()
		self.remove_property(self.get_properties()[1])

		# Set defaults
		self.set_name("Perimeter of Square")

	def try_set_value(self, *args):
		# Try to calculate a value
		return self.set_value(self.calculate_rect_perimeter(self.get_properties()[0], self.get_properties()[0]))


class SquareArea(RectangleArea):
	def __init__(self):
		"""Initialise using the rectangle's class but remove the width (b) property"""
		super(SquareArea, self).__init__()
		self.remove_property(self.get_properties()[1])

		# Set defaults
		self.set_name("Area of Square")

	def try_set_value(self, *args):
		# Try to calculate a value
		return self.set_value(self.calculate_rect_area(self.get_properties()[0], self.get_properties()[0]))

# GLOBAL
# List of available classes as types
AVAIL_CLASSES = [
RectanglePerimeter,
RectangleArea,
SquarePerimeter,
SquareArea
]
