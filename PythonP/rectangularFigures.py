import funClasses

class RectanglePerimeter(funClasses.Perimeter):
	"""Perimeter implementation for a rectangle figure"""

	def __init__(self):
		"""Initialise length (a) and width (b)"""
		super(RectanglePerimeter, self).__init__()

		a = funClasses.Length()
		b = funClasses.Length()

		self.add_property(a)
		self.add_property(b)


	def set_value(self, *args):
		"""Assign a single primitive value (same rules as for Length) or with 2 attributes """

		# Check if arguments passed fit the Length assign
		if (super(funClasses.Perimeter, self).set_value(*args) == True):
			return True

		if (len(args) == 2 and args[0] > 0 and args[1] > 0):
			self.properties[0].set_value(args[0])
			self.properties[1].set_value(args[1])
			return True
		else:
			# raise Exception("Wrong amount of args or either value < 0")
			return False

	def get_value(self):
		if (((super(funClasses.Perimeter, self)).get_value()) != -1):
			return self.value

		if (self.properties[0].get_value() != -1 or self.properties[1].get_value() != -1):
			return self.calculate_rect_perimeter()
		else:
			return -1
			# raise Exception("Properties missing") 

	def calculate_rect_perimeter(self):
		a = self.properties[0]
		b = self.properties[1]

		return 2 * (a.get_value() + b.get_value())








