#!/usr/bin/env python

from nodes import Node

class Pop(Node):
    char = "O"
    args = 1
    results = 1
    
    def add_two(self, inp: Node.number):
        return inp+2
    
    def rm_end(self, inp: Node.indexable):
        return inp[:-1]