from nodes import Node

class Chr(Node):
    char = ".C"
    args = 1
    results = 1
    def func(self, num:int):
        """chr(string)"""
        return chr(num)