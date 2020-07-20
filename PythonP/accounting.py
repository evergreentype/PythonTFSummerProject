"""Module dedicated to accounting-related objects"""

# IMPORTS
from typing import List, Type
import funClasses
import mathematics_p
from funClasses import DEFAULT_NEGATIVE_VALUE, DEFAULT_NAME
#


# FUNCTIONAL OBJECTS
class Dividends(mathematics_p.Length):
    def __init__(self):
        """Simple initialisation"""
        mathematics_p.Length.__init__(self)

        self.set_name("Dividends")
        self.set_symbol("D")
        self.set_unit("$")


class Revenues(funClasses.CompositeMathObject, mathematics_p.Length):
    def __init__(self):
        """Currently does not have properties"""
        funClasses.CompositeMathObject.__init__(self)

        # Set defaults
        self.set_name("Revenue")
        self.set_symbol("R")
        self.set_unit("$")

    def try_set_value(self, *args):
        return -1


class Expenses(funClasses.CompositeMathObject, mathematics_p.Length):
    def __init__(self):
        """Currently does not have properties"""
        funClasses.CompositeMathObject.__init__(self)

        # Set defaults
        self.set_name("Expense")
        self.set_symbol("E")
        self.set_unit("$")

    def try_set_value(self, *args):
        return -1


class NetIncome(funClasses.CompositeMathObject):
    # Set defaults
    __name = "Net income"
    __symbol = "NI"
    __unit = "$"

    def __init__(self):
        """Initialise Revenue and Expense objects and add them to properties"""
        funClasses.CompositeMathObject.__init__(self)

        # Add properties
        __revenues = Revenues()

        __expenses = Expenses()

        self.add_property(__revenues)
        self.add_property(__expenses)

        # Add expression
        __expr0 = funClasses.Expression(
            expressionStr="{r} - {e}",
            **{'r': self.get_properties()[0], 'e': self.get_properties()[1]})

        self.add_expression(__expr0)

    def try_set_value(self, *args):
        # Try to calculate a value
        try:
            self.set_value(self.calculate_netIncome(
                self.get_properties()[0], self.get_properties()[1]))
            return 0
        except:
            pass

        return -1

    def calculate_netIncome(self, _revenues, _expenses):
        """Calculate a net income"""
        revenues = _revenues.get_value()
        expenses = _expenses.get_value()

        try:
            return revenues - expenses
        except Exception as e:
            raise e


class RetainedEarnings(funClasses.CompositeMathObject):
    def __init__(self):
        """Initialise Revenue and Expense objects and add them to properties"""
        funClasses.CompositeMathObject.__init__(self)

        # Set defaults
        self.set_name("Retained Earnings")
        self.set_symbol("RE")
        self.set_unit("$")

        # Add properties
        __netIncome = NetIncome()
        __dividends = Dividends()

        self.add_property(__netIncome)
        self.add_property(__dividends)

        # Add expression
        __expr0 = funClasses.Expression(
            expressionStr="{ni} - {d}",
            **{'ni': self.get_properties()[0], 'd': self.get_properties()[1]})

        self.add_expression(__expr0)

    def try_set_value(self, *args):
        # Try to calculate a value
        try:
            self.set_value(self.calculate_retainedEarnings(
                self.get_properties()[0], self.get_properties()[1]))
            return 0
        except:
            pass

        return -1

    def calculate_retainedEarnings(self, _netIncome, _dividends):
        """Calculate a net income"""
        netIncome = _netIncome.get_value()
        dividends = _dividends.get_value()

        try:
            return netIncome - dividends
        except Exception as e:
            raise e


class Liabilities(funClasses.CompositeMathObject):
    def __init__(self):
        """It has no properties at this implementation"""
        funClasses.CompositeMathObject.__init__(self)

        # Set defaults
        self.set_name("Liabilities")
        self.set_symbol("L")
        self.set_unit("$")

    def try_set_value(self, *args):
        return -1


class StockholdersEquity(funClasses.CompositeMathObject):
    def __init__(self):
        """Initialise Common stock and Retained Earnings objects and add them to properties"""
        funClasses.CompositeMathObject.__init__(self)

        # Set defaults
        self.set_name("Stockholder's Equity")
        self.set_symbol("SE")
        self.set_unit("$")

        # Add properties
        __RE = RetainedEarnings()
        __commonStock = mathematics_p.Length()

        # Initialise Common Stock object
        __commonStock.set_name("Common Stock")
        __commonStock.set_symbol("CS")
        __commonStock.set_unit("$")

        self.add_property(__RE)
        self.add_property(__commonStock)

        # Add expression
        __expr0 = funClasses.Expression(
            expressionStr="{RE} + {CS}",
            **{'RE': self.get_properties()[0], 'CS': self.get_properties()[1]})

        self.add_expression(__expr0)

    def try_set_value(self, *args):
        # Try to calculate a value
        try:
            self.set_value(self.calculate_SE(
                self.get_properties()[0], self.get_properties()[1]))
            return 0
        except:
            pass

        return -1

    def calculate_SE(self, _RE, _commonStock):
        """Calculate Stockholder's Equity"""
        RE = _RE.get_value()
        commonStock = _commonStock.get_value()

        try:
            return RE + commonStock
        except Exception as e:
            raise e


class Assets(funClasses.CompositeMathObject):
    def __init__(self):
        """Initialise Stockholder's Equity and Liabilities objects and add them to properties"""
        funClasses.CompositeMathObject.__init__(self)

        # Set defaults
        self.set_name("Assets")
        self.set_symbol("A")
        self.set_unit("$")

        # Add properties
        __L = Liabilities()
        __SE = StockholdersEquity()

        self.add_property(__L)
        self.add_property(__SE)

        # Add expression
        __expr0 = funClasses.Expression(
            expressionStr="{L} + {SE}",
            **{'L': self.get_properties()[0], 'SE': self.get_properties()[1]})

        self.add_expression(__expr0)

    def try_set_value(self, *args):
        # Try to calculate a value
        try:
            self.set_value(self.calculate_SE(
                self.get_properties()[0], self.get_properties()[1]))
            return 0
        except:
            pass

        return -1

    def calculate_SE(self, _liabilities, _SE):
        """Calculate Stockholder's Equity"""
        liabilities = _liabilities.get_value()
        SE = _SE.get_value()

        try:
            return liabilities + SE
        except Exception as e:
            raise e


# GLOBAL
# List of available classes as types
AVAIL_CLASSES: List[Type] = [
    NetIncome,
    RetainedEarnings,
    StockholdersEquity,
    Assets
]
