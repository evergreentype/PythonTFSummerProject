import funClasses
from funClasses import DEFAULT_NEGATIVE_VALUE

class RectanglePerimeter(funClasses.Perimeter):
	"""Perimeter implementation for a rectangle figure"""

	def __init__(self):
		"""Initialise length (a) and width (b) and add them to properties """
		super(funClasses.Perimeter, self).__init__()

		a = funClasses.Length()
		b = funClasses.Length()

		self.add_property(a)
		self.add_property(b)

	def set_value(self, flag, *args):
		"""Assign a single primitive value (same rules as for Length) or with 2 attributes """

		# Try to assign a value to itself
		if (flag == True):
			if ((len(args) >= 1) and self.validate_value(args[0]) == True):
				self.value = args[0]
				return True

		# Try to assign arguments as values to a and b
		elif (len(args) == 2):
			if ((self.properties[0].validate_value(args[0]) == False) or (self.properties[1].validate_value(args[1]) == False)):
				return False
			
			self.properties[0].set_value(args[0])
			self.properties[1].set_value(args[1])

			print(flag)
			print(args)

			# Try to calculate a value
			return self.set_value(True, self.calculate_rect_perimeter())
		else:
			return False

	def get_value(self):
		"""Return a value if it is set using the same rules as for the Length"""
		if (self.value != DEFAULT_NEGATIVE_VALUE):
			return self.value
		else:
			return DEFAULT_NEGATIVE_VALUE
			# OLD raise Exception("Properties missing") 

	def calculate_rect_perimeter(self):
		"""Standard formula for calculating a rectangle's perimeter"""
		a = self.properties[0].get_value()
		b = self.properties[1].get_value()

		return 2 * (a + b)







