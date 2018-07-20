import funClasses, rectangularFigures

# STRUCTURE TAKEN FROM Tutorial/artem.py and Tutorial/artemTest.py

# Run the tests
runTest = (1,2)
testsDict = {}

def do_test_1():
	"""Test rectangle's perimeter"""
	testVal2 = rectangularFigures.RectanglePerimeter()
	testVal1 = rectangularFigures.RectanglePerimeter()
	testVal1.set_value(True, 5)
	testVal2.set_value(False, 4, 3)

	print('# Rectangle perimeter: ')
	print('From value 5: ' + str(testVal1.get_value()))
	print('From input a=4 and b=3: ' + str(testVal2.get_value()))
testsDict.update({1: do_test_1})

def do_test_2():
	"""Test square's perimeter"""
	testVal1 = rectangularFigures.SquarePerimeter()
	testVal2 = rectangularFigures.SquarePerimeter()
	testVal1.set_value(True, 7)
	testVal2.set_value(False, 3)

	print('# Square perimeter: ')
	print('From value 7: ' + str(testVal1.get_value()))
	print('From input a=3: ' + str(testVal2.get_value()))
testsDict.update({2: do_test_2})






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
