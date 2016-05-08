#!/usr/bin/env python

from nodes import Node

class PuncSplit(Node):
    char = ".c"
    args = 1
    results = 1
    
    @Node.test_func(["I went to the shop."], [["I", "went", "to", "the", "shop"]])
    @Node.test_func(["bob-bob is sad."], [["bob-bob", "is", "sad"]])
    @Node.test_func(["Why?"], [["Why"]])
    @Node.test_func(["He, She, It."], [["He", "She", "It"]])
    def split(self, inp:str):
        """Split by space and remove punctuation"""
        inp = inp.split()
        rtn = []
        for i in inp:
            if i.endswith("..."):
                i = i[:-3]
            if i[-1] in ".,;'\"!?\\/])}":
                i = i[:-1]
            if i[0] in "[({":
                i = i[1:]
            rtn.append(i)
        return [rtn]
        