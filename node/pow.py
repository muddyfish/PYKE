#!/usr/bin/env python

from nodes import Node

class Pow(Node):
    char = "^"
    args = 2
    results = 1
    func = pow