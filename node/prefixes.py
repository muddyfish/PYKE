from nodes import Node


class Prefixes(Node):
    char = ".>"
    args = 1
    results = 1

    @Node.test_func(["abcd"], [["a", "ab", "abc", "abcd"]])
    @Node.test_func([[1, 2, 3, 4]], [[[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]])
    def func(self, a: Node.indexable):
        """Get all the possible prefixes of `a`"""
        rtn = []
        for i in range(len(a)):
            rtn.append(a[:i+1])
        return [rtn]
