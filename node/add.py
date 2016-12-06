#!/usr/bin/env python

from nodes import Node
from type.type_infinite_list import DummyList


class Add(Node):
    """
    Takes two items from the stack and adds them
    """
    char = "+"
    args = 2
    results = 1

    @Node.test_func([[1,2], [3,4]], [[1,2,3,4]])    
    @Node.prefer
    def join_sequence(self, a:Node.sequence, b:Node.sequence):
        """Add 2 sequences together.
The returned type is the same as the first arg"""
        return[type(a)(list(a)+list(b))]

    @Node.test_func([[1,2,3],0], [[1,2,3,0]])   
    @Node.prefer
    def append_sequence(self, a:Node.sequence, b):
        """Same as a.append(b). Works with tuples"""
        return[type(a)(list(a)+[b])]
        
    @Node.test_func([4,[1,2,3]], [[4,1,2,3]])
    @Node.prefer
    def prepend_sequence(self, a, b:Node.sequence):
        """[a]+b. Works with tuples"""
        return[type(b)([a]+list(b))]
    
    @Node.test_func(["test", 1], ["test1"])
    def append_str(self, a:str,b):
        """Appends a non-sequence to a string"""
        return a+str(b)
    
    @Node.test_func([2, "test"], ["2test"])
    def prepend_str(self, a,b:str):
        """Prepends a non-sequence to a string"""
        return str(a)+b
    
    @Node.test_func([1,2], [3])
    def func(self, a,b):
        """Adds two objects together - vanilla addition"""
        return a+b

    def sort_join_inf_list(self, a: Node.infinite, b: Node.infinite):
        def sort_join():
            cur_a = next(a)
            cur_b = next(b)
            while 1:
                if cur_a <= cur_b:
                    yield cur_a
                    cur_a = next(a)
                else:
                    yield cur_b
                    cur_b = next(b)
        return DummyList(sort_join())