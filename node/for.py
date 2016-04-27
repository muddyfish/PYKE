import lang_ast
from nodes import Node
from node.numeric_literal import NumericLiteral
import copy

class For(Node):
    char = "F"
    args = None
    results = None
    contents = 1
    
    def __init__(self, args, ast):
        self.args = args
        self.ast = ast
        if self.ast.nodes == []:
            self.ast.add_node("\n")
        
    @Node.test_func([[1,5]], [[2,10]], "}")
    @Node.test_func([[1,5], 2], [[4,12]], "2}+")
    @Node.test_func([3, 2], [0,2,4], "2*")
    def func(self, *args):
        """Constant arg - how many items off the stack to take, default 1
arg1 - object to iterate over (if int, range(arg1))
Returns a list of lists to the stack"""
        args = list(args)
        args = copy.deepcopy(args)
        is_int = isinstance(args[0], int)
        if is_int:
            args[0] = list(range(args[0]))
        max_len = len(args[0])
        for i, arg in enumerate(args):
            if i == 0: continue
            args[i] = [arg]*max_len
        results = []
        for i in zip(*args):
            rtn = self.ast.run(list(i))
            if len(rtn) == 1: rtn = rtn[0]
            results.append(rtn)
        if not is_int:
            return [results]
        return results
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            new_code, digits = NumericLiteral.accepts(code[1:])
            if new_code is None:
                digits = cls.contents
                code = code[1:]
            else:
                digits = digits([])[0]
                code = new_code
            ast = lang_ast.AST()
            code = ast.setup(code)
            return code, cls(digits, ast)
        return None, None