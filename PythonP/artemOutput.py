import funClasses, rectangularFigures

# STRUCTURE TAKEN FROM Tutorial/artem.py and Tutorial/artemTest.py

# Run the tests
runTest = (5,)
testsDict = {}


# Print functions
def inline_print(xObject=None, tempLst=None):
	"""placeholder"""

	# Rectangle Area from value: 10 unit
	# Rectangle Area from input (l=2 and w=5): 10 unit

	outputStr = xObject.get_name()

	# Test if it is Composite type
	tempLst = list()
	if (isinstance(xObject, funClasses.Composite)):
		# BUG: Messes up output
		tempLst = [(property.get_value(), property.get_name()) for property in xObject.get_properties() 
		if (property.get_value() != None)]

	if (len(tempLst) > 0):
		outputStr += " from input ( "
		
		for (value, name) in tempLst:
			outputStr += name + "=" + str(value) + " "
		
		outputStr += "): "
		tempLst.clear()
	else:
		outputStr += " from value: "
	
	outputStr += str(xObject.get_value())

	outputStr += " " + xObject.get_unit()

	print(outputStr)


# Main Block
print("ARTEM'S TESTS")
def do_test_1():
	"""Test rectangle's perimeter"""
	testVal1 = rectangularFigures.RectanglePerimeter()
	testVal2 = rectangularFigures.RectanglePerimeter()
	testVal1.set_value(True, 5)
	testVal2.set_value(False, 4, 3)

	print("# " + testVal1.get_name() + ": ")
	print('From value 5: ' + str(testVal1.get_value()) + ' ' + testVal1.get_unit())
	print('From input l=4 and w=3: ' + str(testVal2.get_value()) + ' ' + testVal2.get_unit())
testsDict.update({1: do_test_1})

def do_test_2():
	"""Test square's perimeter"""
	testVal1 = rectangularFigures.SquarePerimeter()
	testVal2 = rectangularFigures.SquarePerimeter()
	testVal1.set_value(True, 7)
	testVal2.set_value(False, 3)

	print("# " + testVal1.get_name() + ": ")
	print('From value 7: ' + str(testVal1.get_value()) + ' ' + testVal1.get_unit())
	print('From input l=3: ' + str(testVal2.get_value()) + ' ' + testVal2.get_unit())
testsDict.update({2: do_test_2})

def do_test_3():
	"""Test rectangle's area"""
	testVal1 = rectangularFigures.RectangleArea()
	testVal2 = rectangularFigures.RectangleArea()
	testVal1.set_value(True, 13)
	testVal2.set_value(False, 9, 5)

	print("# " + testVal1.get_name() + ": ")
	print('From value 13: ' + str(testVal1.get_value()) + ' ' + testVal1.get_unit())
	print('From input l=9 w=5: ' + str(testVal2.get_value()) + ' ' + testVal2.get_unit())
testsDict.update({3: do_test_3})

def do_test_4():
	"""Test square's area"""
	testVal1 = rectangularFigures.SquareArea()
	testVal2 = rectangularFigures.SquareArea()
	testVal1.set_value(True, 3)
	testVal2.set_value(False, 12)

	print("# " + testVal1.get_name() + ": ")
	print('From value 3: ' + str(testVal1.get_value()) + ' ' + testVal1.get_unit())
	print('From input l=12: ' + str(testVal2.get_value()) + ' ' + testVal2.get_unit())
testsDict.update({4: do_test_4})

def do_test_5():
	"""Test square's area"""
	testVal1 = rectangularFigures.RectanglePerimeter()
	testVal2 = rectangularFigures.RectangleArea()
	testVal3 = rectangularFigures.SquarePerimeter()

	testVal1.set_value(False, 4, 7)
	testVal2.set_value(True, 13)
	testVal3.set_value(False, 44)

	inline_print(testVal1)
	inline_print(testVal2)
	inline_print(testVal3)
testsDict.update({5: do_test_5})


# Print methods
def start_of_part_print(testNumber):
    print(f'### Test {testNumber}')

def end_of_part_print(testNumber):
    print(f'### End of Test {testNumber}' + '\n')


# Iterate
for i in runTest:
    if i in testsDict:
        # Part title
        start_of_part_print(i)
        
        # Call the corresponding function
        testsDict[i]()
        
        # End of the part
       	end_of_part_print(i)
