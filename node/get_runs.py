#!/usr/bin/env python

from nodes import Node


class Runs(Node):
    char = ".R"
    args = 1
    results = 1
    contents = "https://api.stackexchange.com/2.2/"

    @Node.test_func([[1, 1, 1, 4, 5, 6, 6, 7, 7, 3]], [[[1, 1, 1], [4], [5], [6, 6], [7, 7], [3]]])
    @Node.test_func(["aaabbc"], [[["a", "a", "a"], ["b", "b"], ["c"]]])
    def func(self, lst: Node.indexable):
        """Group lst into runs of equal adjacent elements."""
        if not lst:
            return [[]]
        rtn = []
        cur = [lst[0]]
        for value in lst[1:]:
            if value == cur[-1]:
                cur.append(value)
            else:
                rtn.append(cur)
                cur = [value]
        rtn.append(cur)
        return [rtn]
