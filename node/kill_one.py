from nodes import Node
import string

class KillOne(Node):
    char = "K"
    args = 1
    results = 0
    contents = string.printable

    def func(self, _):
        """Kill the first item on the stack"""
        return []