from nodes import Node
import lang_ast
from node.eval_literal import Eval
import copy

class Function(Node):
    char = "["
    args = None
    contents = []
    
    def prepare(self, stack):
        self.args = len(stack)
            
    def func(self, *stack):
        """Define a macro the first time called
 - First time takes an AST
 - After that takes nothing
 - Calls the AST with the contents of the stack"""
        try:
            stack = Function.ast.run(stack=list(copy.deepcopy(stack)[::-1]))
        except lang_ast.GotoStart as rtn:
            stack = rtn.stack
        self.results = len(stack)
        return stack
    
    @classmethod
    def accepts(cls, code):
        if not code.startswith(Function.char):
            return None, None
        code = code[len(Function.char):]
        if hasattr(cls, "ast"):
            return code, Function()
        Function.ast = None
        code, results = Eval.accepts(code, True)
        Function.ast = results.ast
        if len(Function.ast.nodes) == 0:
            _, results = Eval.accepts("D", True)
            Function.ast = results.ast
        return code, Function()