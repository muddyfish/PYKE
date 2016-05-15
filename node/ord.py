from nodes import Node

class Ord(Node):
    char = ".o"
    args = 1
    results = 1
    def func(self, string:str):
        """ord(string)"""
        return ord(string)