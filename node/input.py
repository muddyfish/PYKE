#!/usr/bin/env python

from nodes import Node

class Input(Node):
    char = "z"
    args = 0
    results = 1
    contents = ""
    def func(self):
        print("Getting input: ")
        return input() or Input.contents