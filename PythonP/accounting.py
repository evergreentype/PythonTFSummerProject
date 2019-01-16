import funClasses
from funClasses import DEFAULT_NEGATIVE_VALUE, DEFAULT_NAME

# FUNCTIONAL OBJECTS


class Line1(funClasses.Length):
    """Perimeter implementation for a rectangle figure"""

    def __init__(self):
        """Initialise length and width and add them to get_properties()"""
        funClasses.Length.__init__(self)

        self.set_symbol("l1")


class RectangleArea(funClasses.Area):
    def __init__(self):
        """Initialise length and width and add them to get_properties()"""
        funClasses.Area.__init__(self)

        # Set defaults
        self.set_name("Area of Rectangle")
        self.set_symbol("A_rect")

        # Add properties
        __l = funClasses.Length()
        __l.set_name("Length")
        __l.set_symbol("l")

        __w = funClasses.Length()
        __w.set_name("Width")
        __w.set_symbol("w")

        self.add_property(__l)
        self.add_property(__w)

        # Add expression
        __expr0 = funClasses.Expression(
            expressionStr="{l} * {w}",
            **{'l': self.get_properties()[0], 'w': self.get_properties()[1]})

        self.add_expression(__expr0)

    def try_set_value(self, *args):
        # Try to calculate a value
        if (DEFAULT_NEGATIVE_VALUE != self.set_value(self.calculate_rect_area(self.get_properties()[0], self.get_properties()[1]))):
            return 0

        return -1

    def calculate_rect_area(self, _l, _w):
        """Standard formula for calculating a rectangle's area"""
        l = _l.get_value()
        w = _w.get_value()

        try:
            return l * w
        except:
            return DEFAULT_NEGATIVE_VALUE


class CuboidVolume(funClasses.Volume):
    def __init__(self):
        """Initialise length and width and add them to get_properties()"""
        funClasses.Volume.__init__(self)

        # Set defaults
        self.set_name("Volume of Cuboid")
        self.set_symbol("V_cuboid")

        # Add properties
        __l = funClasses.Length()
        __l.set_name("Length")
        __l.set_symbol("l")

        __w = funClasses.Length()
        __w.set_name("Width")
        __w.set_symbol("w")

        __h = funClasses.Length()
        __h.set_name("Height")
        __h.set_symbol("h")

        __base = RectangleArea()
        __base.set_name("Base Area")
        __base.set_symbol("A(base)")

        self.add_property(__l)
        self.add_property(__w)
        self.add_property(__h)
        self.add_property(__base)

        # Add expressions
        __expr0 = funClasses.Expression(
            expressionStr="{l} * {w} * {h}",
            **{'l': self.get_properties()[0], 'w': self.get_properties()[1], 'h': self.get_properties()[2]})
        self.add_expression(__expr0)

        __expr1 = funClasses.Expression(
            expressionStr="{base} * {h}",
            **{'base': self.get_properties()[3], 'h': self.get_properties()[2]})
        self.add_expression(__expr1)

    def try_set_value(self, *args):
        # Try to calculate a value
        try:
            # From sides
            if (self.set_value(self.calculate_cuboid_volume(self.get_properties()[0], self.get_properties()[1], self.get_properties()[2]))):
                return 0
        except:
            pass

        try:
            # From base
            if (self.set_value(self.calculate_cuboid_volume_2(self.get_properties()[3], self.get_properties()[2]))):
                return 1
        except:
            pass

    def calculate_cuboid_volume(self, _l, _w, _h):
        """Calculate from the sides"""
        l = _l.get_value()
        w = _w.get_value()
        h = _h.get_value()

        try:
            return l * w * h
        except:
            return DEFAULT_NEGATIVE_VALUE

    def calculate_cuboid_volume_2(self, _base, _h):
        """Calculate from the sides"""
        b = _base.get_value()
        h = _h.get_value()

        try:
            return b * h
        except:
            return DEFAULT_NEGATIVE_VALUE


# GLOBAL
# List of available classes as types
AVAIL_CLASSES = [
    Line1,
    CuboidVolume
]
