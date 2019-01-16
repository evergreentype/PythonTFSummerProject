import math

# Shorter from Fundamental Classes

# GLOBAL CONSTANTS
# Global constant for initial value initialisation for positive values
DEFAULT_NEGATIVE_VALUE = -1
# Global constant for initial name initialisation
DEFAULT_NAME = "Value"
# Global dictonary for setting units
DEFAULT_UNITS = {1: "units", 2: "units^2", 3: "units^3"}
# Global constant for number formatting
DEFAULT_FLOAT_FORMAT = ".2f"
# Global standard value for not set state of __expressionUsed
DEFAULT_EXPRESSION_USED = -1
# Global constant for error message
DEFAULT_ERROR_STR = "Error: "

# CORE CLASSES


class MathObject:
    """Base abstract class inherited by all primitives.

    Implementation of get-, set- and validate-value methods required; init method must set values to defaults. It is not supposed to be initialised directly"""

    def __init__(self):
        """Declare base values"""

        # Name (string)
        self.__name = None
        # Symbol
        self.__symbol = None
        # Unit (dictionary value)
        self.__unit = None

    # Built-in methods
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_symbol(self, symbol):
        self.__symbol = symbol

    def get_symbol(self):
        return self.__symbol

    def set_unit(self, unit):
        self.__unit = unit

    def get_unit(self):
        return self.__unit


class PrimitiveMathObject(MathObject):

    def __init__(self):
        """Declare base values"""
        MathObject.__init__(self)

        # Digital value
        self.__value = None

    # Implementation methods for value operations
    def set_value(self, val):
        raise NotImplementedError(
            "Must implement method set_value(self, *args)")

    def get_value(self):
        raise NotImplementedError("Must implement method get_value(self)")

    def validate_value(self, input):
        raise NotImplementedError(
            "Must implement method validate_value(self, input)")


class Composite(MathObject):
    """Base abstract class that identifies composite objects (objects with properties and expressions).

    Supports adding and removing elements for the list of properties and expressions. It is not supposed to be initialised directly"""

    def __init__(self):
        MathObject.__init__(self)

        # A list that consists of other MathObject or Composite objects
        self.__properties = []

        # A list that consists of Expression objects
        self.__expressions = []

        # Integer value
        self.__expressionUsed = DEFAULT_EXPRESSION_USED

    # Built-in methods
    def add_property(self, prop):
        """Pass an object of any derived class from either MathObject or Composite"""
        self.__properties.append(prop)

    def remove_property(self, prop):
        """Remove an element by its value, raise exception if failed"""
        try:
            self.__properties.remove(prop)
        except Exception:
            raise Exception("Could not remove from Properties list")

    def get_properties(self):
        return self.__properties

    def add_expression(self, expr):
        """Add an Expression object to Expressions list"""
        self.__expressions.append(expr)

    def remove_expression(self, expr):
        """Remove an element by its value, raise exception if failed"""
        try:
            self.__expressions.remove(expr)
        except Exception:
            raise Exception("Could not remove from Expressions list")

    def get_expressions(self):
        return self.__expressions

    def set_expressionUsed(self, exprNum):
        self.__expressionUsed = exprNum

    def get_expressionUsed(self):
        return self.__expressionUsed


class CompositeMathObject(Composite, PrimitiveMathObject):
    """Base abstract class that combines a primitive (i.e. has a value) and composite (i.e. has properties) types.

    It is not supposed to be initialised directly"""

    def __init__(self):
        Composite.__init__(self)
        PrimitiveMathObject.__init__(self)

    def try_set_value(self, *args):
        """Implement calculating a value from properties"""
        raise NotImplementedError(
            "Must implement method assign_properties(self, *args)")


class Length(PrimitiveMathObject):
    """1D primitive"""

    def __init__(self):
        PrimitiveMathObject.__init__(self)

        self.__value = DEFAULT_NEGATIVE_VALUE
        self.set_name("Length")
        self.set_unit(DEFAULT_UNITS[1])

    def set_value(self, val):
        """Accepts a single positive value"""

        if (val == None):
            return False

        try:
            self.validate_value(val)
            self.__value = float(val)
            return True
        except Exception as e:
            raise e

    def get_value(self):
        """Returns a single positive value or a negative -1, if value is not set"""
        if (self.__value != None and self.__value >= 0):
            return self.__value
        else:
            raise ValueError("Value not set")

    def validate_value(self, input):
        """Validate if input exists, is a float and has >= 0 value"""
        try:
            if (float(input) >= 0):
                pass
            else:
                raise ValueError("Value out of range")
        except Exception as c:
            raise c


class Perimeter(CompositeMathObject, Length):
    """Inherits properties of a one-dimentional line, but is able to have properties"""

    def __init__(self):
        CompositeMathObject.__init__(self)

        self.set_name(DEFAULT_NAME)
        self.set_symbol("P")
        self.set_unit(DEFAULT_UNITS[1])


class Area(CompositeMathObject, Length):
    """Abstract 2D concept"""

    def __init__(self):
        CompositeMathObject.__init__(self)

        self.set_name(DEFAULT_NAME)
        self.set_symbol("A")
        self.set_unit(DEFAULT_UNITS[2])


class Volume(CompositeMathObject, Length):
    """Abstract 3D concept"""

    def __init__(self):
        CompositeMathObject.__init__(self)

        self.set_name(DEFAULT_NAME)
        self.set_symbol("V")
        self.set_unit(DEFAULT_UNITS[3])


class Expression:
    def __init__(self, expressionStr, xName="By formula", xDesc="", **epxressionKeys):
        """Set values when initialising the object"""

        # Specifying name is recommended if more than 1 expression associate to the same object
        self.name = xName

        # Add description for additional clarity
        self.desc = xDesc

        """Write mathematical expression in the "exression string"
		Specify names of the variables with "key values" (see string specifier below)"""
        self.expr_str = expressionStr

        """Bind implementation independent "key values" to object references
		'key values' must correspond to those used in the expression string attribute"""
        self.keys = epxressionKeys

    def get_properties(self):
        return [value for value in (self.keys).values()]

    def get_symbolic(self):
        """Receive a dictionary with properties' symbols instead of objects"""
        exprKeys = (self.keys).copy()

        for key, value in exprKeys.items():
            # Replace each value in the dictionary with symbols
            exprKeys[key] = value.get_symbol()

        return exprKeys

    def get_values(self):
        """Receive a dictionary with properties' values instead of objects"""
        exprKeys = (self.keys).copy()

        for key, value in exprKeys.items():
            # Replace each value in the dictionary with symbols
            exprKeys[key] = value.get_value()

        return exprKeys

    def add_format(self, format_specifier):
        """Inserts format specifier that helps display numeric data"""

        format_specifier += '}'
        expr_str_format = self.expr_str.replace(
            '}', ':{Format}'.format(Format=format_specifier))

        return expr_str_format
