#!/usr/bin/env python
from nodes import Node


class FloorDiv(Node):
    char = "f"
    args = 2
    results = 1
    
    @Node.test_func([3, 2], [1])
    @Node.test_func([6, -3], [-2])
    def func(self, a:Node.number,b:Node.number):
        """a/b. Rounds down, returns an int."""
        return a//b
    
    
    @Node.test_func(["134", 1], [["134"]])
    @Node.test_func(["1234", 2], [["12", "34"]])
    @Node.test_func(["1234", 3], [["1", "2", "34"]])
    @Node.test_func([[4,8,15,16,23,42], 5], [[[4],[8],[15],[16],[23,42]]])
    @Node.test_func(["123456789", 5], [['1', '2', '3', '4', '56789']])
    @Node.test_func([[4,8,15,16,23,42], 7], [[[],[],[],[],[],[],[4,8,15,16,23,42]]])
    def chunk(self, inp:Node.indexable, num:int):
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
    
    @Node.test_func([[4, 4, 2, 2, 9, 9], [0, -2, 0, 7, 0]], [[[4],[4,2],[2,9,9]]])
    def split_at(self, inp:Node.indexable, splits:Node.indexable):
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