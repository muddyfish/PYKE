#!/usr/bin/env python

from nodes import Node

class Mod(Node):
    char = "%"
    args = 2
    results = 1
    
    def modulo(self, a:int,b:int):
        return a%b
    
    def every(self, seq:Node.indexable, b:int):
        return seq[::b]