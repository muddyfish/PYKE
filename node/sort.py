#!/usr/bin/env python

from nodes import Node

class Sort(Node):
    char = "S"
    args = 1
    results = 1
    
    @Node.test_func([[2,3,4,1]], [[1,2,3,4]])
    @Node.test_func(["test"], ["estt"])
    def func(self, a: Node.indexable):
        """sorted(a) - returns the same type as given"""
        if isinstance(a, tuple):
            return [tuple(Sort.sort_list(list(a)))]
        if isinstance(a, str):
            return "".join(sorted(a))
        return [Sort.sort_list(a)]
    
    @staticmethod
    def sort_list(a, deep_sort = True):
        if isinstance(a, (str, float, int, complex)):return a
        key = [lambda x:(str(type(x)), x),
               lambda x:(str(type(x)), Sort.sort_list(x))][deep_sort]
        return sorted(a, key = key)
    
    @Node.test_func([3], [[1,2,3]])
    def one_range(self, a:int):
        """range(1,a)"""
        return [list(range(1,a+1))]
    