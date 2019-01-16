import copy
import funClasses
import rectangularFigures
import accounting
from funClasses import DEFAULT_FLOAT_FORMAT, DEFAULT_EXPRESSION_USED, DEFAULT_ERROR_STR


# FUNCTIONS
def process_selection(xObject, force=False, level=1):
    """Receive input from primitive or force Composite type to receive input (force = True), or iterate through properties to set values"""

    # Max number of "-" to print
    separatorConst = 8

    # Received value; validation bool; indentation string
    valInput, valid, indent = None, False, ' '*(level)

   # If the object is a primitive (or forced), receive value as a primitive
    if ((isinstance(xObject, funClasses.Composite) == False) or (force == True)):
        print(indent + "# " + xObject.get_name() +
              " (" + xObject.get_unit() + "):")
        while valid != True:
            try:
                # Receive input
                valInput = input(indent + xObject.get_symbol() + " = ")

                # Try to set it
                xObject.set_value(valInput)
                valid = True
            except Exception as e:
                # Print exception string
                print(indent + DEFAULT_ERROR_STR + str(e))

        # End recursion
        return

    # For a Composite object, print options
    print("-"*level + str(level) + "-"*(separatorConst - level))
    print(indent + "Find " + xObject.get_name() + ", " + xObject.get_symbol())
    print(indent + "# Select an option:")
    print(indent + "1: From value")
    i = 2

    for expression in xObject.get_expressions():
        print(indent + "{:d}".format(i) + ": " + expression.name + ": " +
              expression.expr_str.format(**(expression.get_symbolic())))
        i += 1

    # Receive input
    usrInput = -1
    while usrInput not in range(1, i):
        usrInput = int(input(indent + "-> "))

    # Input from value is selected
    if (usrInput == 1):
        # Force Composite object to receive a primitive
        process_selection(xObject, True, level)
    # Input by Expression is selected
    else:
        # Iterate through the properties and set their values
        for property in xObject.get_expressions()[usrInput-2].get_properties():
            process_selection(property, False, level + 1)

        # Try to set the Composite value
        expressionUsed = xObject.try_set_value()

        # Set what expression was used for calculating a composite value
        xObject.set_expressionUsed(expressionUsed)

    # Create a copy and fetch an answer
    # Reference: http://effbot.org/pyfaq/how-do-i-copy-an-object-in-python.htm
    tempObj = copy.deepcopy(xObject)
    levelAnswer = print_answer(tempObj)

    # Print answer
    if (level == 1):
        print(indent + "Final Answer:")
    else:
        print(indent + "Intermediate Output:")
    print(indent + levelAnswer)

    print("-"*level + str(level) + "e" + "-"*(separatorConst - level - 1))


def print_answer(xObject):
    """Print a to-calculate variable, expression used for calculation and found value with units"""

    left_side, middle_expr_symb, middle_expr_float, right_side = None, None, None, None

    # Compose the left part: found mathematical object
    left_side = xObject.get_symbol()

    if (isinstance(xObject, funClasses.Composite) == True):
        # Fetch the middle part: expression used
        middle_expr_symb = fetch_expressions(xObject, str, False)
        middle_expr_float = fetch_expressions(xObject, float, False)

    # Compose the right part: answer value and units
    right_side = "{answer:{Format}}".format(answer=xObject.get_value(
    ), Format=DEFAULT_FLOAT_FORMAT) + " " + xObject.get_unit()

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

    return answerStr


def fetch_expressions(xObject, of_type, force, level=0):
    """Compose a string of Expressions values and return it. 
    The fetching is based on finding what expression was used (__expressionUsed) for finding the value and replacing symbols with their due properties. 
    For example: In formula [ V_cuboid = A(base) * h ], if A(base) was found by its values [ a * b ], its symbol, A(base), is substituted with its properties' symbols or values. 
    The method returns a complete concatenated string.

    To fill the of_type arg, pass data-type keyword (like str or float).
    level=0 indicates the top level of recursion, different formatting rules apply to it"""

    # If the object is a primitive (or forced), return value as a primitive
    if ((isinstance(xObject, funClasses.Composite) == False) or (force == True)):
        # Do not return anything if on the top level
        if (level == 0):
            return None

        # Decide which formatting option to use
        if (of_type == str):
            return xObject.get_symbol()
        elif (of_type == float):
            return ('{:' + DEFAULT_FLOAT_FORMAT + '}').format(xObject.get_value())

    if (isinstance(xObject, funClasses.Composite) == True):
        exprUsed = xObject.get_expressionUsed()

        # Force Composite object to return a value
        if (exprUsed == DEFAULT_EXPRESSION_USED):
            return fetch_expressions(xObject, of_type, True, level)

        compositeStr = ''

        if (level != 0):
            compositeStr += '('
        expr = xObject.get_expressions()[exprUsed]

        # Iterative through the properties and set their values
        for value in expr.get_properties():
            value.set_symbol(fetch_expressions(value, of_type, False, 1))

        compositeStr += expr.expr_str

        if (level != 0):
            compositeStr += ')'

        compositeStr = compositeStr.format(**(expr.get_symbolic()))

        return compositeStr


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

    # Make calculation of the choice
    print("  Calculation:")
    process_selection(objects[usrInput])

    # Repeat
    print("")
    main_menu(objTypes)


# INVOKE MENU
main_menu(accounting.AVAIL_CLASSES)
