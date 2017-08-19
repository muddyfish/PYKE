import copy

from nodes import Node
from type.type_infinite_list import DummyList


class DeepForApply(Node):
    char = "a"
    args = 1
    results = 1
    contents = "".join(chr(i)for i in range(256))
    
    def __init__(self, ast: Node.EvalLiteral):
        self.ast = ast
        if self.ast.nodes == []:
            self.ast.add_node(b"\n")
    
    @Node.test_func([[[(0, 0), (0, 1)], [(1, 0), (1, 1)]]], [[[1, 2], [2, 3]]], "+h")
    def func(self, seq: Node.sequence):
        """Deeply apply a node to a nD tree"""
        return [self.recurse(seq)]

    def recurse(self, seq):
        if isinstance(seq[0][0], Node.sequence):
            return [self.recurse(i) for i in seq]
        else:
            rtn = []
            for i in copy.deepcopy(seq):
                try:
                    val = self.ast.run(list(i))
                except AssertionError:
                    val = self.ast.run([list(i)])
                if len(val) > 1: rtn.append(val)
                else: rtn.extend(val)
            return rtn

    def apply_values(self, dic:dict, *args):
        """for value, key in dic:
    dic[key] = eval_literal(value)"""
        rtn = {}
        for key in dic:
            val = self.ast.run([dic[key], key, *args])
            rtn[key] = val
        return [rtn, *args]


    def inf_list(self, base: (int, float, str)):
        def iterate():
            cur = [base]
            while 1:
                cur = self.ast.run(cur)
                if len(cur) == 1:
                    yield cur[0]
                else:
                    yield cur
        return DummyList(iterate())
