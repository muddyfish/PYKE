from node.map import Map

class LeftMap(Map):
    char = "L"
    args = 0
    results = None
    contents = -1
    
    def prepare(self, stack):
        if len(stack) == 0:
            self.add_arg(stack)
        if isinstance(stack[0], dict):
            self.args = max(1, self.args-2)
        old_call = self.node.__call__
        self.node.__call__ = lambda *args:old_call(*reversed(args))
    
for func in LeftMap.get_functions():
    if hasattr(func, "tests"):
        delattr(func, "tests")