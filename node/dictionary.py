#!/usr/bin/env python

import json
import os

import __main__

from nodes import Node


class Dictionary(Node):
    char = ".d"
    args = 0
    results = 1
    
    def __init__(self, word_ids: Node.IntList):
        self.setup()
        self.words = " ".join(Dictionary.word_list[i] for i in word_ids)
        
    def func(self):
        """Lookup a list of english words in the built in dictionary. Use `/dictionary` for a compressor"""
        return self.words

    @classmethod
    def setup(cls):
        if not hasattr(cls, "word_list"):
            filename = os.path.join(os.path.split(__main__.__file__)[0], "PeriodicTableJSON.json")
            cls.word_list = init_words(filename)

    @staticmethod
    def compress(inp):
        words = init_words()
        inp_words = [word.lower()for word in inp.split(" ")]
        rtn = chr(len(inp_words))
        for word in inp_words:
            if word not in words:
                rtn += "Word %s not in wordlist" % word
            else:
                rtn += chr(words.index(word))
        return rtn


def init_words(dict_file):
    with open(dict_file) as words_f:
        return json.load(words_f)
