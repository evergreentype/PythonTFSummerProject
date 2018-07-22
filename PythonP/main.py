import funClasses, rectangularFigures
from funClasses import DEFAULT_FLOAT_FORMAT

# FUNCTIONS
def process_selection(xObject, ignore = False):
	"""Receive input from primitive or force Composite type to receive input (ignore = True) or iterate through properties to set values"""

	valInput, valid = None, False

	# If the object is a primitive (or forced), receive value as a primitive
	if ((isinstance(xObject, funClasses.Composite) == False) or (ignore == True)):
		print(xObject.get_name() + " (" + xObject.get_unit() + "):")
		while valid != True:
			valInput = input("-> ")
			valid = xObject.set_value(valInput)

		# Break recursion
		return

	# If the object is Composite, print additional options
	print("### Choose:")
	print("1: input from value")
	print("2: calculate (from " +  ", ".join([property.get_name() for property in xObject.get_properties()]) + ")")

	usrInput = -1
	while usrInput not in range(1, 3):
		usrInput = int(input("-> "))
	print("###")

	# Input from value is selected
	if (usrInput == 1):
		# Force Composite object to receive a primitive
		process_selection(xObject, True)
	# Input by calculation was selected
	elif (usrInput == 2):
		# Iterative through the properties and set their values
		for property in xObject.get_properties():
			process_selection(property, False)

		# Try to set the Composite value
		xObject.try_set_value()


def print_formula(xObject):
	left_side = xObject.get_symbol()
	right_side = str(xObject.get_value()) + " " + xObject.get_unit()

	print(left_side + " = " + right_side)


def main_menu(objTypes):
	"""Print the main menu while not terminated by input 0"""

	print("# Select from the options:")
	# Instantiate and print all options
	objects = []
	i = 0
	for objType in objTypes:
		objects.append(objType())
		print(str(i+1) + ": " + objects[i].get_name())
		i += 1
	print("0: exit")

	# Receive and validate input
	usrInput = -1
	while usrInput not in range(0, i+1):
		usrInput = int(input("-> "))

	# Terminate if needed
	if (usrInput == 0):
		return
	else:
		usrInput -= 1

	# Print find options
	print("## To find " + objects[usrInput].get_name() + ": ")
	process_selection(objects[usrInput])

	# Print answer
	print("## Answer: ")
	print_formula(objects[usrInput])
	print("##")

	# Repeat
	print("#\n")
	main_menu(objTypes)


# INVOKE
main_menu(rectangularFigures.AVAIL_CLASSES)
