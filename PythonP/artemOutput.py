import funClasses, rectangularFigures
import numbers

# STRUCTURE TAKEN FROM Tutorial/artem.py and Tutorial/artemTest.py

# Run the tests
runTest = (8,)
testsDict = {}

# Main Block
print("ARTEM'S TESTS")
def do_test_8():
	"""Test inheritance from math classes and lambda functions"""
	class myPrimitive(numbers.Number):
		def __new__(cls, val, *args, **kwargs):
			return  super(myPrimitive, cls).__new__(cls, val)

	a = myPrimitive(3) + myPrimitive(13)

	print(a)
testsDict.update({8: do_test_8})





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

def print_inline(xObject):
	"""Print a line for either a primitive value or calculated value"""

	outputStr = None
	tempLst = list()

	# Test if it is Composite type
	if (isinstance(xObject, funClasses.Composite)):
		tempLst = [(property.get_value(), property.get_name()) for property in xObject.get_properties() 
		if (property.get_value() != None)]

	# Format the string if calculated from its properties
	if (len(tempLst) > 0):
		outputStr = "Calculated ("
		
		for (value, name) in tempLst:
			outputStr += name + "=" + "{:.2f}".format(value) +  ","
		
		outputStr += "): "
	else:
		outputStr = "Input from value: "
	
	# Format and display answer
	outputStr += "\n" + "{:.2f}".format(xObject.get_value())
	outputStr += " (" + xObject.get_unit() + ")"

	print(outputStr)

def do_test_5():
	"""Does not work after updates"""
	testVal1 = rectangularFigures.RectanglePerimeter()
	testVal2 = rectangularFigures.RectangleArea()
	testVal3 = rectangularFigures.SquarePerimeter()

	testVal1.set_value(False, 4, 7)
	testVal2.set_value(True, 13)
	testVal3.set_value(False, 44)

	print_inline(testVal1)
	print_inline(testVal2)
	print_inline(testVal3)
testsDict.update({5: do_test_5})


def do_test_6():
	"""Test string formatting"""

	# P(rect) = 2 * (l + w)
	# From values: 2 * (length + width)
	# From values: 2 * (4 + 5)

	strTest = "{len:{Format}} + {wid:{Format}}"
	lengthStr = "length"
	length = 3.333333333333
	widthStr = "width"
	width = 4.44444444444
	floatFormat = "{:.2f}"

	isStr = True
	if (isStr):
		floatFormat = ""
	else:
		floatFormat = ".2f"

	#print(strTest.format(wid = width, l = length, Format = floatFormat))
	#print(strTest.format(wid = widthStr, l = lengthStr, Format = floatFormat))

	tuples = []
	tupItem = {"expressionStr":strTest, "l":length, "w":width}
	tuples.append(tupItem)
	print(tuples[0])

	def print_str_form(xStr, **xFormatSp):
		xFormatSp["Format"] = ""
		print(xStr.format(**xFormatSp))

	dictTemp = {'len':widthStr, 'wid':lengthStr, 'anDict': {1: "he", 2:"be"}}

	dictVals = [val for val in dictTemp.values()]
	print("dictVals: ")
	print(dictVals)

	print("Print str form:")
	print_str_form(strTest, **dictTemp)
testsDict.update({6: do_test_6})


def do_test_7():
	"""Debugging Area classes"""

	testIns = rectangularFigures.RectangleArea()

	print("RectangleArea object:")
	print(testIns)
	print("RectangleArea properties:")
	print(testIns.get_properties())
	print("RectangleArea expressions:")
	print(testIns.get_expressions()[0].expr_str)

	testIns.get_properties()[0].set_value(5)
	print("Property 0: " + str(testIns.get_properties()[0].get_value()))

	testIns.get_properties()[1].set_value(6)
	print("Property 1: " + str(testIns.get_properties()[1].get_value()))

	print(testIns.try_set_value())

	print("Value: " + str(testIns.get_value()))


testsDict.update({7: do_test_7})

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
