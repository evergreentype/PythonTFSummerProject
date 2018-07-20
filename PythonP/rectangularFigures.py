import funClasses

class RectanglePerimeter(funClasses.Perimeter):
	"""Perimeter implementation for a rectangle figure"""

	def __init__(self):
		"""Initialise length (a) and width (b) and add them to properties """
		super(RectanglePerimeter, self).__init__()

		a = funClasses.Length()
		b = funClasses.Length()

		self.add_property(a)
		self.add_property(b)


	def set_value(self, *args):
		"""Assign a single primitive value (same rules as for Length) or with 2 attributes """

		# Check if arguments passed are for the Length assignment
		if (super(funClasses.Perimeter, self).set_value(*args) == True):
			return True

		# Else, try to assign arguments as values to a and b
		if (len(args) == 2 and args[0] > 0 and args[1] > 0):
			self.properties[0].set_value(args[0])
			self.properties[1].set_value(args[1])

			# Try to calculate a value
			return self.set_value(self.calculate_rect_perimeter())
		else:
			# OLD raise Exception("Wrong amount of args or either value < 0")
			return False

	def get_value(self):
		"""Return a value if it is set using the same rules as for the Length"""
		if (((super(funClasses.Perimeter, self)).get_value()) != DEFAULT_NEGATIVE_VALUE):
			return self.value
		else:
			return DEFAULT_NEGATIVE_VALUE
			# OLD raise Exception("Properties missing") 

	def calculate_rect_perimeter(self):
		"""Standard formula for calculating a rectangle's perimeter"""
		a = self.properties[0]
		b = self.properties[1]

		return 2 * (a.get_value() + b.get_value())








