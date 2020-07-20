""" Shorter from Fundamental Classes """

# IMPORTS
from __future__ import annotations
from typing import List, Dict, Optional, Union
from abc import ABC, abstractmethod
#


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
#


# CORE CLASSES
class MathObject(ABC):
    """Base abstract class inherited by all primitives.

    Implementation of get-, set- and validate-value methods required; init method must set values to defaults. It is not supposed to be initialised directly"""

    # Name (string)
    __name: str
    # Symbol
    __symbol: str
    # Unit (dictionary value)
    __unit: str

    # Built-in methods
    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_symbol(self, symbol: str):
        self.__symbol = symbol

    def get_symbol(self) -> str:
        return self.__symbol

    def set_unit(self, unit: str):
        self.__unit = unit

    def get_unit(self) -> str:
        return self.__unit


class PrimitiveMathObject(MathObject):

    # Digital value
    __value: Optional[float] = None

    def __init__(self):
        """Declare base values"""
        # MathObject.__init__(self)

    # Implementation methods for value operations
    def set_value(self, val: str):
        try:
            self.validate_value(val)
            self.__value = float(val)
        except Exception as e:
            raise e

    def get_value(self) -> Optional[float]:
        """Return a single float value or None, if value is not set"""
        try:
            self.validate_value(self.__value)
            return self.__value
        except Exception as e:
            raise e

    def validate_value(self, input: Union[float, None, str]) -> None:
        try:
            if (input != None and float(input) != None):
                pass
            else:
                raise ValueError("No value passed")
        except Exception as c:
            raise c


class Composite(MathObject, ABC):
    """Base abstract class that identifies composite objects (objects with properties and expressions).

    Supports adding and removing elements for the list of properties and expressions. It is not supposed to be initialised directly."""

    # A list that consists of other MathObject or Composite objects
    __properties: List[Union[MathObject, Composite]] = []
     # A list that consists of Expression objects
    __expressions: List[Expression] = []

    # Integer value
    __expressionUsed: int = DEFAULT_EXPRESSION_USED

    def __init__(self):
        MathObject.__init__(self)

    # Built-in methods
    def add_property(self, prop: Union[MathObject, Composite]):
        """Pass an object of any derived class from either MathObject or Composite"""
        self.__properties.append(prop)

    def remove_property(self, prop: Union[MathObject, Composite]):
        """Remove an element by its value, raise exception if failed"""
        try:
            self.__properties.remove(prop)
        except Exception:
            raise Exception("Could not remove from Properties list")

    def get_properties(self):
        return self.__properties

    def add_expression(self, expr: Expression):
        """Add an Expression object to Expressions list"""
        self.__expressions.append(expr)

    def remove_expression(self, expr: Expression):
        """Remove an element by its value, raise exception if failed"""
        try:
            self.__expressions.remove(expr)
        except Exception:
            raise Exception("Could not remove from Expressions list")

    def get_expressions(self):
        return self.__expressions

    def set_expressionUsed(self, exprNum: int):
        self.__expressionUsed = exprNum

    def get_expressionUsed(self) -> int:
        return self.__expressionUsed


class CompositeMathObject(Composite, PrimitiveMathObject, ABC):
    """Base abstract class that combines a primitive (i.e. has a value) and composite (i.e. has properties) types.

    It is not supposed to be initialised directly"""

    def __init__(self):
        Composite.__init__(self)
        PrimitiveMathObject.__init__(self)

    @abstractmethod
    def try_set_value(self, *args: List):
        """Implement calculating a value from properties"""
        raise NotImplementedError(
            "Must implement method assign_properties(self, *args)")


class Expression:
    # Specifying name is recommended if more than 1 expression associate to the same object
    name: str
    # Description for additional clarity
    desc: str
    """Write mathematical expression in the "exression string"
		Specify names of the variables with "key values" (see string specifier below)"""
    expr_str: str
    """Bind implementation independent "key values" to object references
        'key values' must correspond to those used in the expression string attribute"""
    keys: Dict[str, PrimitiveMathObject]

    def __init__(self, expressionStr: str, xName: str = "By formula", xDesc: str = "", **epxressionKeys):
        """Set values when initialising the object"""

        # Specifying name is recommended if more than 1 expression associate to the same object
        self.name = xName
        self.desc = xDesc
        self.expr_str = expressionStr

        self.keys = epxressionKeys

    def get_properties(self):
        return [value for value in (self.keys).values()]

    def get_symbolic(self) -> Dict[str, str]:
        """Receive a dictionary with properties' symbols instead of objects"""
        
        exprKeys: Dict[str, str] = {}

        for key, value in self.keys.items():
            # Replace each value in the dictionary with symbols
            exprKeys[key] = value.get_symbol()

        return exprKeys

    def get_values(self):
        """Receive a dictionary with properties' values instead of objects"""

        exprKeys = {}

        for key, value in self.keys.items():
            # Replace each value in the dictionary with symbols
            exprKeys[key] = value.get_value()

        return exprKeys

    def add_format(self, format_specifier: str) -> str:
        """Inserts format specifier that helps display numeric data"""

        format_specifier += '}'
        expr_str_format = self.expr_str.replace(
            '}', ':{Format}'.format(Format = format_specifier))

        return expr_str_format
