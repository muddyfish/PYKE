#!/usr/bin/env python

from nodes import Node
import math

class End(Node):
    char = "e"
    args = 1
    results = 1
    contents = math.e
    
    def complement(self, inp: Node.number):
        return ~inp
    
    def first(self, inp: Node.indexable):
        return inp[-1]