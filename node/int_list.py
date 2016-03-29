import lang_ast
from nodes import Node

class IntList(Node):
    char = "u"
    args = 0
    results = None
    contents = "0123456789"
    
    def __init__(self, value):
        self.value = value
        
    @Node.test_func([], [1,42,64], "#!J`")
    def func(self):
        """length = ord(`arg`[0])-32
return [ord(a)-32 for a in `arg`[1:length+1]]"""
        return self.value
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.value)
        
    @classmethod
    def accepts(cls, code, accept = False):
        if accept: code = "u"+code
        if code == "" or\
           (code[0] != cls.char): return None, None
        value = ord(code[1])-32
        lst = [ord(i)-32 for i in code[2:2+value]]
        return code[2+value:], cls(lst)
    