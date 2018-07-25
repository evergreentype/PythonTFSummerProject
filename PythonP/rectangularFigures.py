import funClasses
from funClasses import DEFAULT_NEGATIVE_VALUE, DEFAULT_NAME


# FUNCTIONAL CLASSES
class RectanglePerimeter(funClasses.Perimeter):
	"""Perimeter implementation for a rectangle figure"""

	def __init__(self):
		"""Initialise length and width and add them to get_properties()"""
		super(RectanglePerimeter, self).__init__()

		# Set defaults
		self.set_name("Perimeter of Rectangle")
		self.set_symbol("P(rect)")

		# Add properties
		__l = funClasses.Length()
		__w = funClasses.Length()
		__l.set_name("Length")
		__w.set_name("Width")
		__l.set_symbol("l")
		__w.set_symbol("w")

		self.add_property(__l)
		self.add_property(__w)

		# Add expression
		__expr0 = funClasses.Expression(
			expressionStr = "2 * ({l:{Format}} + {w:{Format}})",
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

		return 2 * (l + w)


class RectangleArea(funClasses.Area):
	def __init__(self):
		"""Initialise length and width and add them to get_properties()"""
		super(RectangleArea, self).__init__()

		# Set defaults
		self.set_name("Area of Rectangle")
		self.set_symbol("A(rect)")

		# Add properties
		__l = funClasses.Length()
		__w = funClasses.Length()
		__l.set_name("Length")
		__w.set_name("Width")
		__l.set_symbol("l")
		__w.set_symbol("w")

		self.add_property(__l)
		self.add_property(__w)

		# Add expression
		__expr0 = funClasses.Expression(
			expressionStr = "{l:{Format}} * {w:{Format}}",
			**{'l':self.get_properties()[0], 'w':self.get_properties()[1]})
		self.add_expression(__expr0)

	def try_set_value(self, *args):
		# Try to calculate a value
		if (self.set_value(self.calculate_rect_area(self.get_properties()[0], self.get_properties()[1]))):
			return 0

		return -1

	def calculate_rect_area(self, _l, _w):
		"""Standard formula for calculating a rectangle's area"""
		l = _l.get_value()
		w = _w.get_value()

		return l * w


class SquarePerimeter(RectanglePerimeter):
	def __init__(self):
		"""Initialise using the rectangle's class but remove the width property"""
		super(SquarePerimeter, self).__init__()
		self.remove_property(self.get_properties()[1])

		# Set defaults
		self.set_name("Perimeter of Square")
		self.set_symbol("P(square)")

		# Add expression
		self.remove_expression(self.get_expressions()[0])
		
		__expr0 = funClasses.Expression(
			expressionStr = "4 * {l:{Format}}",
			**{'l':self.get_properties()[0]})
		self.add_expression(__expr0)


	def try_set_value(self, *args):
		# Try to calculate a value
		if (self.set_value(self.calculate_rect_perimeter(self.get_properties()[0], self.get_properties()[0]))):
			return 0

		return -1


class SquareArea(RectangleArea):
	def __init__(self):
		"""Initialise using the rectangle's class but remove the width property"""
		super(SquareArea, self).__init__()
		self.remove_property(self.get_properties()[1])

		# Set defaults
		self.set_name("Area of Square")
		self.set_symbol("A(square)")

		# Add expression
		self.remove_expression(self.get_expressions()[0])
		
		__expr0 = funClasses.Expression(
			expressionStr = "{l:{Format}} * {l:{Format}}",
			**{'l':self.get_properties()[0]})
		self.add_expression(__expr0)

	def try_set_value(self, *args):
		# Try to calculate a value
		if (self.set_value(self.calculate_rect_area(self.get_properties()[0], self.get_properties()[0]))):
			return 0

		return -1

# GLOBAL
# List of available classes as types
AVAIL_CLASSES = [
RectanglePerimeter,
RectangleArea,
SquarePerimeter,
SquareArea
]
