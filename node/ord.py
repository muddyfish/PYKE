from node.dictionary import Dictionary
from nodes import Node


class Ord(Node):
    char = ".o"
    args = 1
    results = 1

    def ord(self, string: str):
        """ord(string)"""
        try:
            return ord(string)
        except TypeError:
            return [[ord(i)for i in string]]

    def lookup(self, word_id: int):
        Dictionary.setup()
        return Dictionary.word_list[word_id]