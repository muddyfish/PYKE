#!/usr/bin/env python

from nodes import Node
import json

class Dictionary(Node):
    char = ".d"
    args = 0
    results = 1
    
    def __init__(self, word_ids:Node.IntList):
        if not hasattr(Dictionary, "word_list"):
            Dictionary.word_list = init_words()
        self.words = " ".join(Dictionary.word_list[i] for i in word_ids)
        
    def func(self):
        return self.words
    
    def compress(inp):
        words = init_words()
        inp_words = [word.lower()for word in inp.split(" ")]
        rtn = chr(len(inp_words))
        for word in inp_words:
            assert(word in words)
            rtn += chr(words.index(word))
        return rtn
    
def init_words(dict_file = "dictionary.json"):
    words_f = open(dict_file)
    words = json.load(words_f)
    words_f.close()
    return words
