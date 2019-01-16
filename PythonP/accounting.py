import funClasses
from funClasses import DEFAULT_NEGATIVE_VALUE, DEFAULT_NAME

# ABSTRACT OBJECTS
class Rectangle(funClasses.Composite):
	def __init__(self):
		funClasses.Composite.__init__(self)

		# Set
		self.set_name("Rectangle")
		self.set_symbol("rect")




# FUNCTIONAL OBJECTS
class RectanglePerimeter(funClasses.Perimeter):
	"""Perimeter implementation for a rectangle figure"""

	def __init__(self):
		"""Initialise length and width and add them to get_properties()"""
		funClasses.Perimeter.__init__(self)

		# Set defaults
		self.set_name("Perimeter of Rectangle")
		self.set_symbol("P_rect")

		# Add properties
		__l = funClasses.Length()
		__l.set_name("Length")
		__l.set_symbol("l")

		__w = funClasses.Length()
		__w.set_name("Width")
		__w.set_symbol("w")

		self.add_property(__l)
		self.add_property(__w)

		# Add expression
		__expr0 = funClasses.Expression(
			expressionStr = "2 * ({l} + {w})",
			**{'l':self.get_properties()[0], 'w':self.get_properties()[1]})

		self.add_expression(__expr0)

	def try_set_value(self, *args):
		# Try to calculate a value
		if (self.set_value(self.calculate_rect_perimeter(self.get_properties()[0], self.get_properties()[1]))):
			return 0

		return -1

	def calculate_rect_perimeter(self, _l, _w):
		"""Standard formula for calculating a rectangle's perimeter"""
		l = _l.get_value()
		w = _w.get_value()

		try:
			return 2 * (l + w)
		except:
			return DEFAULT_NEGATIVE_VALUE


# GLOBAL
# List of available classes as types
AVAIL_CLASSES = [
RectanglePerimeter
]
