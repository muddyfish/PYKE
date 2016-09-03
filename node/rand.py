#!/usr/bin/env python
import random

from nodes import Node

class Random(Node):
    char = "H"
    args = 1
    results = 1
    
    def random_choice(self, inp:Node.indexable):
        """Choose one in a list randomly"""
        return [random.choice(inp)]
        
    def randint(self, inp:int):
        """Random number between 0 and inp inclusive"""
        return random.randint(0,inp)