#!/usr/bin/env python

from nodes import Node

class Mod(Node):
    char = "%"
    args = 2
    results = 1
    
    def modulo(self, a:Node.number,b:Node.number):
        """a%b"""
        return a%b
    
    def every(self, seq:Node.indexable, b:int):
        """seq[::b]"""
        return seq[::b]