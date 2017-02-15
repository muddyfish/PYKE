#!/usr/bin/env python

import datetime

import ephem

from nodes import Node


class Pow(Node):
    """
    Takes two items from the stack and raises a^b
    """
    char = "^"
    args = 2
    results = 1
    

    @Node.test_func([3,2], [9])
    @Node.test_func([2,-2], [0.25])
    def func(self, a: Node.number, b: Node.number):
        """a**b"""
        return a**b
    
    @Node.test_func(["Test.", "."], [1])
    @Node.test_func(["Test.", "?"], [0])
    @Node.test_func(["Test.", "t."], [1])
    def endswith(self, string: str, suffix: str):
        """Does string end with suffix?"""
        return int(string.endswith(suffix))
    
    @Node.test_func([[1, 2, 3, 4, 5], [10, 10, 4, 62, 7]], [22167])
    @Node.test_func([[4, 2], [5, 10]], [42])
    @Node.test_func([[3, 0, 7], [5, 1, 10]], [37])
    def mixed_base(self, inp: Node.sequence, bases: Node.sequence):
        """Convert from a mixed base number to an integer"""
        prod = 1
        for val in bases:
            prod *= val
        cur = 0
        for e, i in enumerate(inp):
            prod //= bases[e]
            cur += i*prod
        return cur

    @Node.test_func(["abc", 5], ["abc  "])
    @Node.test_func(["abc", 2], ["abc"])
    @Node.test_func(["te  ", 6], ["te    "])
    def lpad(self, string: str, amount: int):
        """Return string padded with spaces to make it `amount` in length"""
        return string.ljust(amount)

    def get_distance_to_sun(self, time: Node.clock, object: str):
        """Gets the distance to the sun from `object` at `time`"""
        new_time = datetime.datetime(*time.time_obj[:7])

        return getattr(ephem, object)(new_time).sun_distance

    @Node.test_func([[1, 2, 6, 7], 5], [6])
    @Node.test_func([[-1, 0, 1], 0], [0])
    @Node.test_func([[-1, 1], 0], [-1])
    def closest_to(self, lst: Node.sequence, value: Node.number):
        """Given a list of numbers, return the closest one to `value`.
If 2 numbers are of the same distance, the one closest to the start of the original list is returned"""
        return sorted(lst, key=lambda i: abs(i-value))[0]
