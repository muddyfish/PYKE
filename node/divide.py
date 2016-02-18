#!/usr/bin/env python
from __future__ import division

from nodes import Node

class Divide(Node):
    char = "/"
    args = 2
    results = 1
    def func(self, a,b):
        return a/b