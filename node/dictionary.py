#!/usr/bin/env python

import json

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
            cls.word_list = init_words()

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
    
def init_words(dict_file = "dictionary.json"):
    words_f = open(dict_file)
    words = json.load(words_f)
    words_f.close()
    return words
