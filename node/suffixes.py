from nodes import Node


class Suffixes(Node):
    char = ".>"
    args = 1
    results = 1

    @Node.test_func(["abcd"], [["d", "cd", "bcd", "abcd"]])
    @Node.test_func([[1, 2, 3, 4]], [[[4], [3, 4], [2, 3, 4], [1, 2, 3, 4]]])
    def func(self, a: Node.indexable):
        """Get all the possible suffixes of `a`"""
        rtn = []
        for i in range(len(a)):
            rtn.append(a[i:])
        return [rtn[::-1]]
