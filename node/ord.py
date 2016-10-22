from nodes import Node

class Ord(Node):
    char = ".o"
    args = 1
    results = 1

    def func(self, string:str):
        """ord(string)"""
        try:
            return ord(string)
        except TypeError:
            return [[ord(i)for i in string]]