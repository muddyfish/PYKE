#!/usr/bin/env python

from nodes import Node

class Pow(Node):
    """
    Takes two items from the stack and raises a^b
    """
    char = "^"
    args = 2
    results = 1
    func = pow