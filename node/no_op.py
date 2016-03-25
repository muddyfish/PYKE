#!/usr/bin/env python

from nodes import Node

class NoOp(Node):
    char = " "
    contents = " "
    def func(self):
        pass
    