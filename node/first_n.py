from nodes import Node


class FirstN(Node):
    char = ".f"
    args = 2
    results = 1
    contents = 1
    
    def __init__(self, ast: Node.EvalLiteral):
        self.ast = ast
        self.uses_j = self.ast.uses_j
        self.ast.uses_j = False
        
    def prepare(self, stack):
        if len(stack) == 0:
            self.args = 0
        elif len(stack) < 2:
            self.args = 1
    
    @Node.test_func([4,2], [[2,3,4,5]])
    @Node.test_func([3,-1], [[-1,0,2]], "t")
    def first_n_start(self, count: int, start: int):
        """Return first count items where the last element on the returned stack is true"""
        results = []
        i = start
        while len(results) != count:
            if self.uses_j:
                if hasattr(self.ast.j_node, "contents"):
                    old_j = self.ast.j_node.contents
                self.ast.j_node.contents = [len(results)+1]
            rtn = self.ast.run([i])
            try:
                self.ast.j_node.contents = old_j
            except (NameError, UnboundLocalError):
                pass
            if len(rtn) != 0 and rtn[-1]:
                results.append(i)
            i += 1
        if count == 1:
            return results
        return [results]
    
    @Node.test_func([4], [[1,2,3,4]])
    @Node.test_func([4], [[5,6,7,8]], "4>")
    def first_n(self, count: int):
        """return first_n_start(FirstN.contents)"""
        return self.first_n_start(count, FirstN.contents)
    
    @Node.test_func([], [1])
    @Node.test_func([], [5], "4>")
    @Node.is_func
    def first(self):
        """return first_n(1)"""
        return self.first_n(1)
