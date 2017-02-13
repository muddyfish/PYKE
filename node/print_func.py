#!/usr/bin/env python

from nodes import Node
from type.type_infinite_list import CountList, ModifyList


class PrintFunc(Node):
    char = "p"
    args = 1
    results = 1

    contents = ModifyList(CountList(), "_P")

    def func(self, arg):
        """print arg
return arg"""
        print(arg, end="")
        return [arg]