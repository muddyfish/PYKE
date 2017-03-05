#!/usr/bin/env python

import datetime

from dateutil.relativedelta import relativedelta

from node.prime import Prime
from nodes import Node
from type.type_time import TypeTime


class Sum(Node):
    char = "s"
    args = 0
    results = 1
    default_arg = 1
    
    def __init__(self, args: Node.Base10Single):
        self.arg = args
        
    def prepare(self, stack):
        if len(stack) == 0:
            self.add_arg(stack)
        if self.arg == 1 and isinstance(stack[0], int):
            self.func = self.prime
        elif self.arg == 1 and isinstance(stack[0], str):
            self.func = self.palendromise
        elif isinstance(stack[0], Node.clock):
            self.args = 1
        else:
            self.args = self.arg
        if self.arg == 0:
            self.args = len(stack)
        elif not self.overwrote_default:
            if isinstance(stack[0], (list, tuple)):
                self.args = 1
            else:
                self.args = len(stack)
    
    @Node.test_func([1, 2], [3])
    @Node.test_func([[3, 4]], [7])
    @Node.test_func(["t", "e", "s", "t"], ["test"], "0")
    @Node.is_func
    def sum_stack(self, *inp):
        """If no `amount`: return sum(stack)
Else if arg1 is a list, return sum(arg1)
Else return sum(stack[:`amount`])"""
        if self.args == 1:
            inp = inp[0]
        if str in map(type, inp):
            inp = [str(i) for i in inp]
        try:
            current = inp[0]
        except TypeError:
            return sum(inp)
        for val in inp[1:]:
            current += val
        return [current]

    def prime(self, inp: int):
        return Prime.is_prime(inp)

    def palendromise(self, inp: str):
        r_inp = inp[::-1]
        return inp + r_inp[1:]

    def run_infinite(self, inf: Node.infinite):
        return inf.modify(inf.node_map, self.__class__(self.args))

    def inc_time(self, time: Node.clock):
        """Increment a time object by the following amount:
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
        arg_map = (("years", 1),
                   ("months", 1),
                   ("days", 1),
                   ("hours", 1),
                   ("minutes", 1),
                   ("seconds", 1),
                   ("days", 7),
                   ("years", 4),
                   ("years", 10),
                   ("hours", 12))
        args = 2
        if self.overwrote_default:
            args = self.arg
        delta = relativedelta(**dict([arg_map[args]]))
        new_time = datetime.datetime(*time.time_obj[:7]) + delta
        return TypeTime(new_time.timetuple())
