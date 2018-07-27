import funClasses, rectangularFigures
from funClasses import DEFAULT_FLOAT_FORMAT

# FUNCTIONS
def process_selection(xObject, force = False):
	"""Receive input from primitive or force Composite type to receive input (force = True) or iterate through properties to set values"""

	valInput, valid = None, False

	# If the object is a primitive (or forced), receive value as a primitive
	if ((isinstance(xObject, funClasses.Composite) == False) or (force == True)):
		print(xObject.get_name() + ", " + xObject.get_symbol() + " (" + xObject.get_unit() + "):")
		while valid != True:
			valInput = input("-> ")
			valid = xObject.set_value(valInput)

		# End recursion
		return

	# If the object is Composite, print options
	print("## Find " + xObject.get_name() + ":")
	print("1: From value")
	i = 2
	for expression in xObject.get_expressions():
		print("{:d}".format(i) + ": " + expression.name + ": " + expression.expr_str.format(**(expression.get_symbolic())))
		i += 1

	usrInput = -1
	while usrInput not in range(1, i):
		usrInput = int(input("-> "))
	print("## Now enter value(s):")

	# Input from value is selected
	if (usrInput == 1):
		# Force Composite object to receive a primitive
		process_selection(xObject, True)
	# Input by Expression is selected
	else:
		# Iterative through the properties and set their values
		for property in xObject.get_expressions()[usrInput-2].get_properties():
			process_selection(property, False)

		# Try to set the Composite value
		expressionUsed = xObject.try_set_value()

		xObject.set_expressionUsed(expressionUsed)


def fetch_expressions(xObject, of_type, force = False, level = 0):
	"""Compose a string of Expressions values and return it.

	Pass data type keyword (like str or float) to fill the of_type arg
	level=0 indicates the top level of recursion, different formatting rules apply to it"""

	# If the object is a primitive (or forced), return value as a primitive
	if ((isinstance(xObject, funClasses.Composite) == False) or (force == True)):
		# Do not return anything if on the top level
		if (level == 0):
			return None

		# Decide which formatting options to use
		if (of_type == str):
			return xObject.get_symbol()
		elif (of_type == float):
			return ('{:' + DEFAULT_FLOAT_FORMAT + '}').format(xObject.get_value())

	if (isinstance(xObject, funClasses.Composite) == True):
		exprUsed = xObject.get_expressionUsed()

		# Force Composite object to return a value
		if (exprUsed == None):
			return fetch_expressions(xObject, of_type, True, level=1)
		
		compositeStr = ''

		if (level != 0):
			compositeStr  += '('
		expr = xObject.get_expressions()[exprUsed]

		# Iterative through the properties and set their values
		for value in expr.get_properties():
			value.set_symbol(fetch_expressions(value, of_type, level=1))

		compositeStr += expr.expr_str

		if (level != 0):
			compositeStr += ')'

		compositeStr = compositeStr.format(**(expr.get_symbolic()))

		return compositeStr


def print_answer(xObject):
	"""Print a to-calculate variable, expression used for calculation and found value with units"""

	left_side, middle_expr_symb, middle_expr_float, right_side = None, None, None, None
	
	# Compose the left part: found mathematical object
	left_side = xObject.get_symbol()

	if (isinstance(xObject, funClasses.Composite) == True):		
		# Fetch the middle part: formula used
		middle_expr_symb = fetch_expressions(xObject, str)
		middle_expr_float = fetch_expressions(xObject, float)

	# Compose the right part: answer value and units
	right_side = "{answer:{Format}}".format(answer=xObject.get_value(), Format=DEFAULT_FLOAT_FORMAT) + " " + xObject.get_unit()

	# Print
	answerStr = ''
	if (left_side != None):
		answerStr += left_side
		answerStr += " = "

	if (middle_expr_symb != None):
		answerStr += middle_expr_symb
		answerStr += " = "

	if (middle_expr_float != None):
		answerStr += middle_expr_float
		answerStr += " = "

	if (right_side != None):
		answerStr += right_side

	print(answerStr)


def main_menu(objTypes):
	"""Print the main menu while not terminated by input - 0"""

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

	# End recursion if needed
	if (usrInput == 0):
		return
	else:
		usrInput -= 1

	# Print find options
	process_selection(objects[usrInput])

	print("## Answer: ")
	print_answer(objects[usrInput])
	print("##")

	# Repeat
	print("#\n")
	main_menu(objTypes)


# INVOKE MENU
main_menu(rectangularFigures.AVAIL_CLASSES)
