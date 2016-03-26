#!/usr/bin/env python

from nodes import Node

class Index(Node):
    char = "N"
    args = 2
    results = 1
    
    def index(self, a: str, b: int):
        """a.index(b)"""
        return a.index(b)
    
    def count(self, a: int, b: str):
        """a.count(b)"""
        return a.count(b)
    