#!/usr/bin/env python

import datetime
import math
import string

from dateutil.relativedelta import relativedelta

from nodes import Node
from type.type_time import TypeTime


class Letters(Node):
    char = "l"
    args = 1
    results = 1
    default_arg = 0
    contents = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    settings = [lambda x: x.lower(),
                lambda x: x.upper(),
                lambda x: x.swapcase(),
                lambda x: x.title(),
                lambda x: x.capitalize(),
                lambda x: string.capwords(x),
                lambda x: x.strip(),
                lambda x: x.lstrip(),
                lambda x: x.rstrip()
                ]
    
    def __init__(self, config: Node.Base10Single):
        self.config = config
        
    @Node.test_func([[3,2]], [2], "0")
    @Node.test_func(["Hi!"], ["hi!"], "1")
    @Node.test_func(["Hi!"], ["HI!"], "2")
    @Node.test_func(["Hi!"], ["hI!"], "3")
    @Node.test_func(["hello world"], ["Hello World"], "4")
    @Node.test_func(["hello world"], ["Hello world"], "5")
    @Node.test_func(["hello world"], ["Hello World"], "6")
    @Node.test_func(["  world  "], ["world"], "7")
    @Node.test_func(["  world  "], ["world  "], "8")
    @Node.test_func(["  world  "], ["  world"], "9")
    def func(self, x: Node.dict_indexable):
        """0 - len (floor(log(x)) with numbers)
1 - lower
2 - upper
3 - swapcase
4 - title
5 - capitalize
6 - capwords
7 - strip
8 - lstrip
9 - rstrip"""
        if self.config == 0:
            return self.len(x)
        return Letters.settings[self.config-1](x)
    
    def len(self, x):
        return len(x)

    def factors(self, num: int):
        if num in [0, 1]:
            return [[]]
        if num in [2, 3]:
            return [[num]]
        rtn = []
        end = int(math.sqrt(num))
        for i in range(2, end+1):
            if i == end:
                if num % i == 0:
                    rtn.append(i)
            elif num % i == 0:
                rtn.append(i)
                rtn.append(num//i)
        if rtn:
            return [rtn]
        return [[num]]

    def nth_root(self, num: float):
        conf = 3 or self.config
        return round(num ** (1 / conf), 10)

    def dec_time(self, time: Node.clock):
        """Decrement a time object by the following amount:
0 - years
1 - months
2 - days
3 - hours
4 - minutes
5 - seconds
6 - weeks
7 - 4 years
8 - decades
9 - 12 hours"""
        arg_map = (("years", -1),
                   ("months", -1),
                   ("days", -1),
                   ("hours", -1),
                   ("minutes", -1),
                   ("seconds", -1),
                   ("days", -7),
                   ("years", -4),
                   ("years", -10),
                   ("hours", -12))
        args = 2
        if self.overwrote_default:
            args = self.config
        delta = relativedelta(**dict([arg_map[args]]))
        new_time = datetime.datetime(*time.time_obj[:7]) + delta
        return TypeTime(new_time.timetuple())
