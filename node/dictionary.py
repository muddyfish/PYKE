#!/usr/bin/env python

from nodes import Node
import json

words_f = open("dictionary.json")
words = json.load(words_f)
words_f.close()

class Dictionary(Node):
    char = ".d"
    args = 0
    results = 1
    contents = len(words)
    
    def __init__(self, word_ids:Node.IntList):
        self.words = " ".join(words[i] for i in word_ids)
        
    def func(self):
        return self.words
    
    def compress(inp):
        inp_words = [word.lower()for word in inp.split(" ")]
        rtn = chr(len(inp_words))
        for word in inp_words:
            assert(word in words)
            rtn += chr(words.index(word))
        return rtn