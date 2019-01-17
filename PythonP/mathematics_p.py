"""Module dedicated to base mathematical-related objects"""

# IMPORTS
import funClasses
from funClasses import DEFAULT_NEGATIVE_VALUE, DEFAULT_NAME, DEFAULT_UNITS
#


# FUNCTIONAL CLASSES
class Length(funClasses.PrimitiveMathObject):
    """1D primitive"""

    def __init__(self):
        funClasses.PrimitiveMathObject.__init__(self)

        self.__value = DEFAULT_NEGATIVE_VALUE
        self.set_name("Length")
        self.set_unit(DEFAULT_UNITS[1])

    def set_value(self, val):
        """Accepts a single positive value"""
        try:
            self.validate_value(val)
            self.__value = float(val)
        except Exception as e:
            raise e

    def get_value(self):
        """Return a single positive value or a negative -1, if value is not set"""
        try:
            self.validate_value(self.__value)
            return self.__value
        except Exception as e:
            raise e

    def validate_value(self, input):
        """Validate if input exists, is a float and has >= 0 value"""
        try:
            funClasses.PrimitiveMathObject.validate_value(self, input)

            if (float(input) >= 0):
                pass
            else:
                raise ValueError("Value out of range")
        except Exception as c:
            raise c


class Perimeter(funClasses.CompositeMathObject, Length):
    """Inherits properties of a one-dimentional line, but is able to have properties"""

    def __init__(self):
        funClasses.CompositeMathObject.__init__(self)

        self.set_name(DEFAULT_NAME)
        self.set_symbol("P")
        self.set_unit(DEFAULT_UNITS[1])


class Area(funClasses.CompositeMathObject, Length):
    """Abstract 2D concept"""

    def __init__(self):
        funClasses.CompositeMathObject.__init__(self)

        self.set_name(DEFAULT_NAME)
        self.set_symbol("A")
        self.set_unit(DEFAULT_UNITS[2])


class Volume(funClasses.CompositeMathObject, Length):
    """Abstract 3D concept"""

    def __init__(self):
        funClasses.CompositeMathObject.__init__(self)

        self.set_name(DEFAULT_NAME)
        self.set_symbol("V")
        self.set_unit(DEFAULT_UNITS[3])