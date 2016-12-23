#!/usr/bin/env python

import datetime

import ephem

from nodes import Node


class Product(Node):
    char = "B"
    args = 1
    results = 1
    contents = "><+-.,[]"  # Possible bytes in a BF program
    
    @Node.test_func([[1,2]], [2])
    @Node.test_func([[3,4]], [12])
    @Node.test_func([[3,4,2]], [24])
    def func(self, inp:Node.sequence):
        """return product of integer sequence"""
        current = 1
        for val in inp:
            if isinstance(val, Node.sequence):
                current *= self.func(val)[0]
            else:
                current *= val
        return [current]
    
    def to_int(self, inp:Node.number):
        """Return int(inp)"""
        return int(inp)
    
    @Node.test_func(["HELLO"], [1])
    @Node.test_func(["World7"], [0])
    @Node.test_func(["@"], [0])
    def is_alpha(self, string:str):
        """Is a string alphabetic?"""
        return int(string.isalpha())

    def get_next_full_moon(self, time: Node.clock):
        """Gets the date of the next full moon"""
        new_time = datetime.datetime(*time.time_obj[:7])

        return ephem.next_full_moon(new_time)
