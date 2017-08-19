import copy

from nodes import Node


class DeepFor(Node):
    char = ".F"
    args = None
    results = None
    default_arg = 1
    
    def __init__(self, args: Node.NumericLiteral, ast:Node.EvalLiteral):
        self.args = args
        self.ast = ast
        if self.ast.nodes == []:
            self.ast.add_node(b"\n")
    
    @Node.test_func([[[[0], 1, 2, 3], [4, 5, 6, 7]]], [[[[2], 4, 6, 8], [10, 12, 14, 16]]], "h}")
    @Node.test_func([[1, [[2, 3, [4], 5], 6], 7]], [[2, [[2, 4, [4], 6], 6], 8]], "D 2%+")
    def func(self, *args):
        """Deeply run a for loop across a nD tree.
Takes a list or tuple with a varying depth.
Returns a list with the same depth all round with the function applied."""
        seq, *args = copy.deepcopy(args)
        assert(isinstance(seq, Node.sequence))
        self.type = None
        self.shared_type = False
        rtn = self.recurse(seq, args)
        if self.type is None or self.shared_type:
            return [rtn]
        return [self.recurse(seq, args, run_func=self.cleanup)]

    def recurse(self, seq, args, run_func=None):
        not_overwritten = run_func is None
        if not_overwritten:
            run_func = self.run
        rtn = []
        for i in seq:
            if isinstance(i, Node.sequence):
                if not_overwritten:
                    rtn.append(self.recurse(i, args))
                else:
                    rtn.append(self.recurse(i, args, run_func))
            else:
                rtn.append(run_func(i, args))
                if not_overwritten:
                    self.get_type(rtn[-1])
        return rtn
    
    def run(self, obj, args):
        rtn = self.ast.run([obj]+args)
        if len(rtn) == 1: rtn = rtn[0]
        return rtn
    
    def cleanup(self, obj, args):
        obj = self.run(obj, args)
        if obj:
            return obj
        else:
            return self.type

    def get_type(self, obj):
        if obj:
            rtn_type = {str: "",
                        int: 0,
                        list: [],
                        dict: {},
                        tuple: (),
                        set: set(),
                        bool: False}.get(type(obj), None)
            if self.type is None:
                self.type = rtn_type
            elif self.type == rtn_type:
                pass
            else:
                self.shared_type = True
        return obj
