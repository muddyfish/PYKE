#!/usr/bin/env python
    
from nodes import Node


class NumericLiteral(Node):
    args = 0
    results = 1

    def __init__(self, digits):
        self.digits = digits
        
    @Node.test_func([], [1], "1")
    @Node.test_func([], [1.5], "1.5")
    @Node.test_func([], [0.1], ".1")
    def func(self):
        """Returns a numeric literal, including floats.
Values can't end with a ".", instead use ".0"
The "0" digit gets returned immediately if it is at the beginning."""
        return self.digits

    def __repr__(self):
        return "%s: %s" % (self.__class__.__name__, self.digits)
        
    @classmethod
    def accepts(cls, code, ignore_zeros=False):
        if code == "":
            return None, None
        digits = ""
        while len(code) != 0 and\
                (code[:1] in b".0123456789") and \
                (ignore_zeros or digits != "0"):
            digits += chr(code[0])
            code = code[1:]
        if digits.endswith("."):
            digits = digits[:-1]
            code = b"."+code
        if digits:
            if digits[0] == "0" and digits != "0":    
                return bytearray(code), cls(digits)
            try:
                return bytearray(code), cls(int(digits))
            except ValueError:
                try:
                    return bytearray(code), cls(float(digits))
                except ValueError:
                    return None, None
        return None, None
