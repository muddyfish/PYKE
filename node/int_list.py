import lang_ast
from nodes import Node
from node.base96_single import Base96Single 

class IntList(Node):
    char = "u"
    args = 0
    results = None
    contents = "0123456789"
    
    def __init__(self, value):
        self.value = value
        self.results = len(value)
        
    def func(self):
        return self.value
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.value)
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            new_code, length = Base96Single.accepts("w"+code[1:])
            if new_code is None:
                length = 1
                code = code[1:]
            else:
                length = length([])[0]
                code = new_code
#            print(length)
            return code, cls([length])
        return None, None