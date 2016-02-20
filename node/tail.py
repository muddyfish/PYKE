#!/usr/bin/env python

from nodes import Node

class Tail(Node):
    char = "t"
    args = 1
    results = 1
    
    def sub_one(self, inp: Node.number):
        return inp-1
    
    def first(self, inp: Node.indexable):
        return inp[1:]