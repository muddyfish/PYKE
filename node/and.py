#!/usr/bin/env python

from nodes import Node

@Node.test("&", [1,2], [1])
@Node.test("&", [0,1], [False])
@Node.test("&", ["Hello!", 4], ["Hello!"])
class And(Node):
    char = "&"
    args = 2
    results = 1
    def func(self, a,b):
        return a and b