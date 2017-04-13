#!/usr/bin/env python
import datetime
from itertools import product

import ephem

import nodes
from nodes import Node
from type.type_infinite_list import DummyList


def all_combinations():
    g_contents = nodes.nodes["alphabet"].contents
    i = 0
    while 1:
        i += 1
        yield from map("".join, product(g_contents, repeat=i))


class FloorDiv(Node):
    char = "f"
    args = 2
    results = 1
    contents = DummyList(all_combinations())
    
    @Node.test_func([3, 2], [1])
    @Node.test_func([6, -3], [-2])
    def func(self, a: Node.number, b: Node.number):
        """a/b. Rounds down, returns an int."""
        return a//b

    @Node.test_func(["134", 1], [["134"]])
    @Node.test_func(["1234", 2], [["12", "34"]])
    @Node.test_func(["1234", 3], [["1", "2", "34"]])
    @Node.test_func([[4, 8, 15, 16, 23, 42], 5], [[[4], [8], [15], [16], [23, 42]]])
    @Node.test_func(["123456789", 5], [['1', '2', '3', '4', '56789']])
    @Node.test_func([[4, 8, 15, 16, 23, 42], 7], [[[], [], [], [], [], [], [4, 8, 15, 16, 23, 42]]])
    def chunk(self, inp: Node.indexable, num: int):
        """Return inp seperated into num groups"""
        rtn = []
        size = len(inp)//num
        try:
            for i in range(0, num*size, size):
                rtn.append(inp[i:i+size])
        except ValueError:
            for i in range(num): rtn.append([])
            i = 0
        if len(rtn) != num:
            rtn.append(inp[i+size:])
        else:
            rtn[-1] += inp[i+size:]
        return [rtn]
    
    @Node.test_func([[4, 4, 2, 2, 9, 9], [0, -2, 0, 7, 0]], [[[4], [4, 2], [2, 9, 9]]])
    def split_at(self, inp: Node.indexable, splits: Node.sequence):
        """Split inp at truthy values in splits"""
        rtn = [[]]
        for i, do_split in zip(inp, splits+[0]):
            if do_split: rtn.append([])
            rtn[-1].append(i)
        return [rtn]

    def time_int_div(self, a: Node.clock, b: Node.number):
        return a.floordiv_int(b)

    def time_int_div_2(self, a: Node.number, b: Node.clock):
        return b.floordiv_int(a)

    def time_div(self, a: Node.clock, b: Node.clock):
        return b.floordiv_time(a)

    def combinations(self, length: int, seq: Node.indexable):
        """Return all combinations of `seq` length `length`"""
        return [["".join(a) for a in product(seq, repeat=length)]]

    def get_size(self, time: Node.clock, object: str):
        """Gets the size of the object in arcseconds"""
        new_time = datetime.datetime(*time.time_obj[:7])

        return getattr(ephem, object)(new_time).size
