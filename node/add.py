#!/usr/bin/env python

from nodes import Node

@Node.test("+", [1,2], [3])
@Node.test("+", [0,[1,2,3]], [[1,2,3,0]])
@Node.test("+", [[1,2,3],4], [[4,1,2,3]])
@Node.test("+", [[3,4],[1,2]], [[1,2,3,4]])
class Add(Node):
    """
    Takes two items from the stack and adds them
    """
    char = "+"
    args = 2
    results = 1
    
    @Node.prefer
    def join_sequence(self, a:Node.sequence, b:Node.sequence):
        """Add 2 sequences together.
The returned type is the same as the first arg"""
        return[type(a)(list(a)+list(b))]
    
    @Node.prefer
    def append_sequence(self, a:Node.sequence, b):
        """Same as a.append(b). Works with tuples"""
        return[type(a)(list(a)+[b])]
    
    @Node.prefer
    def prepend_sequence(self, a, b:Node.sequence):
        """[a]+b. Works with tuples"""
        return[type(b)([a]+list(b))]
    
    def append_str(self, a:str,b):
        """Appends a non-sequence to a string"""
        return a+str(b)
    
    def prepend_str(self, a,b:str):
        """Prepends a non-sequence to a string"""
        return str(a)+b
    
    def func(self, a,b):
        """Adds two objects together - vanilla addition"""
        return a+b