#!/usr/bin/env python

from nodes import Node


class Dict2(Node):
    char = ".Y"
    args = 2
    results = 1
    contents = "qwertyuiopasdfghjklzxcvbnm"

    @Node.test_func([["test", "pi"], [2, 3]], [{"test": 2, "pi": 3}])
    @Node.test_func(["abc", [1, 2, 3]], [{"a": 1, "b": 2, "c": 3}])
    def dict(self, keys: Node.indexable, values: Node.indexable):
        """Takes some keys and some values and turn them into a dictionary"""
        return dict(zip(keys, values))
