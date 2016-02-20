import lang_ast
from nodes import Node
from node.numeric_literal import NumericLiteral 

class For(Node):
    """
    Constant arg - how many items off the stack to take, default 1
    arg1 - variable to iterate over
    args - the rest of the args are copied and used as arguments
    """
    char = "F"
    args = 0
    results = None
    
    def __init__(self, args, ast):
        self.args = args
        self.ast = ast
        
    def func(self, *args):
        args = list(args)
        if isinstance(args[0], int):
            args[0] = range(args[0])
        max_len = len(args[0])
        for i, arg in enumerate(args):
            if i == 0: continue
            args[i] = [arg]*max_len
        results = []
        for i in zip(*args):
            rtn = self.ast.run(list(i))
            if len(rtn) == 1: rtn = rtn[0]
            results.append(rtn)
        return results
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            new_code, digits = NumericLiteral.accepts(code[1:])
            if new_code is None:
                digits = 1
                code = code[1:]
            else:
                digits = digits([])[0]
                code = new_code
            ast = lang_ast.AST()
            code = ast.setup(code)
            return code, cls(digits, ast)
        return None, None