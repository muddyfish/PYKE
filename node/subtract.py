#!/usr/bin/env python

from nodes import Node
from type.type_infinite_list import DummyList


class Subtract(Node):
    char = "-"
    args = 2
    results = 1
    contents = "bcdfghjklmnpqrstvwxyz"
    
    @Node.test_func([4, 5], [-1])
    @Node.test_func([42, 7], [35])
    def func(self, a,b):
        """a-b. Vanilla subraction."""
        return a-b
    
    @Node.test_func(["test", "te"], ["s"])
    @Node.test_func(["test", "ts"], ["e"])
    def sub_str(self, a: str, b: str):
        """Remove all characters in b from a."""
        out = a[:]
        for i in b:
            out = out.replace(i, "")
        return out

    def sub_list(self, seq: Node.sequence, remove):
        while remove in seq:
            seq.remove(remove)
        return [seq]

    def sub_list_single(self, seq: Node.sequence, remove: (list, set)):
        for i in remove:
            if i in seq:
                seq.remove(i)
        return [seq]

    @Node.prefer
    def r_pad(self, string: str, amount: int):
        """pad string with spaces to make `amount` long"""
        return string.rjust(amount)

    def sort_remove_inf_list(self, a: Node.infinite, b: Node.infinite):
        def sort_remove():
            cur_a = next(a)
            cur_b = next(b)
            while 1:
                if cur_a < cur_b:
                    yield cur_a
                    cur_a = next(a)
                elif cur_a > cur_b:
                    yield cur_b
                    cur_b = next(b)
                else:
                    cur_a = next(a)
                    cur_b = next(b)
        return DummyList(sort_remove())


