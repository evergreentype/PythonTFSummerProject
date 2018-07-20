import funClasses, rectangularFigures

# STRUCTURE TAKEN FROM Tutorial/artem.py and Tutorial/artemTest.py

# Run the tests
runTest = (1,2,3,4)
testsDict = {}


# Main Block
print("ARTEM'S TESTS")
def do_test_1():
	"""Test rectangle's perimeter"""
	testVal2 = rectangularFigures.RectanglePerimeter()
	testVal1 = rectangularFigures.RectanglePerimeter()
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
