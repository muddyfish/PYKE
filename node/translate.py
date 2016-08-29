#!/usr/bin/env python

from nodes import Node

class Translate(Node):
    char = ".:"
    args = 3
    results = 1
    
    def translate(self, inp:str, find:Node.indexable, replace:Node.indexable):
        """Multiple find and replace"""
        for i in zip(find,replace):
            inp = inp.replace(*i)
        return inp