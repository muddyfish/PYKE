#!/usr/bin/env python

from nodes import Node

class HeadEnd(Node):
    char = "}"
    args = 1
    results = 2
    def func(self, inp):
        return [inp[0], inp[-1]]