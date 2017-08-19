import copy

from node.sort import Sort
from node.transpose_pad import PadTranspose
from nodes import Node


class SortEval(Node):
    char = ".#"
    args = None
    results = None
    default_arg = 1
    
    def __init__(self, args: Node.NumericLiteral, ast:Node.EvalLiteral):
        self.args = args
        self.ast = ast
        if self.ast.nodes == []:
            self.ast.add_node(b"_")
        
    @Node.test_func([[1, 5, 2]], [[5, 2, 1]], "")
    @Node.test_func([[1, 2, 3, 4, 5], [10, 2, 8, 4, 6]], [[2, 4, 5, 3, 1]], "2R")
    def func(self, *args):
        """Sort input values by final outcome of loop"""
        args = list(args)
        args = copy.deepcopy(args)
        is_int = isinstance(args[0], int)
        if is_int:
            args[0] = list(range(args[0]))
        results = []
        packed_args = PadTranspose._transpose(args)[0]
        for i in packed_args:
            rtn = self.ast.run(list(i))
            results.append(rtn)
        sorted_results = Sort.sort_list(results, deep_sort=False)
        return [list(list(zip(*sorted(enumerate(args[0]), key=lambda x:sorted_results.index(results[x[0]]))))[1])]
