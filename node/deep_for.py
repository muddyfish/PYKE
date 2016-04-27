import lang_ast
from nodes import Node
from node.numeric_literal import NumericLiteral
import copy

class DeepFor(Node):
    char = ".F"
    args = None
    results = None
    contents = 1
    
    def __init__(self, args, ast):
        self.args = args
        self.ast = ast
        if self.ast.nodes == []:
            self.ast.add_node("\n")
    
    @Node.test_func([[[[0],1,2,3],[4,5,6,7]]], [[[[2], 4, 6, 8], [10, 12, 14, 16]]], "h}")
    @Node.test_func([[1,[[2,3,[4],5],6],7]], [[2, [[2, 4, [4], 6], 6], 8]], "D 2%+")
    def func(self, *args):
        """Deeply run a for loop across a nD tree.
Takes a list or tuple with a varying depth.
Returns a list with the same depth all round with the function applied."""
        seq, *args = copy.deepcopy(args)
        assert(isinstance(seq,Node.sequence))
        return [self.recurse(seq, args)]

    def recurse(self, seq, args):
        rtn = []
        for i in seq:
            if isinstance(i, Node.sequence):
                rtn.append(self.recurse(i, args))
            else:
                rtn.append(self.run(i, args))
        return rtn
    
    def run(self, obj, args):
        rtn = self.ast.run([obj]+args)
        if len(rtn) == 1: rtn = rtn[0]
        return rtn
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        
    @classmethod
    def accepts(cls, code):
        if code.startswith(cls.char):
            new_code, digits = NumericLiteral.accepts(code[2:])
            if new_code is None:
                digits = cls.contents
                code = code[2:]
            else:
                digits = digits([])[0]
                code = new_code
            ast = lang_ast.AST()
            code = ast.setup(code)
            return code, cls(digits, ast)
        return None, None