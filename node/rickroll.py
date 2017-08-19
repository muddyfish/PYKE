#!/usr/bin/env python

from nodes import Node


class RickRoll(Node):
    char = ".."
    args = 0
    results = 1
    
    def func(self):
        """Redirect to RickRoll"""
        return "Never gonna let you down"
