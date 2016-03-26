#!/usr/bin/env python

from nodes import Node

class Input(Node):
    char = "z"
    args = 0
    results = 1
    contents = ""
    def func(self):
        """input() or Input.contents"""
        print("z: ")
        return input() or Input.contents