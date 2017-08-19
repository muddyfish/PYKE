from nodes import Node

class IntList(Node):
    char = "u"
    args = 0
    results = None
    contents = "0123456789"
    
    def __init__(self, value):
        self.value = value
        
    @Node.test_func([], [[33,74,96]], "\x03!J`")
    def func(self):
        """length = ord(`arg`[0])
return [ord(a) for a in `arg`[1:length+1]]"""
        return [self.value]
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.value)
        
    @classmethod
    def accepts(cls, code, accept=False):
        if accept:
            code = b"u"+code
        if not code:
            return None, None
        if code[0] != cls.char[0]:
            return None, None
        value = code[1]
        lst = []
        code = code[2:]
        for i in range(value):
            lst.append(0)
            new = code[0]
            code = code[1:]
            while new & 0x80:
                lst[-1] |= (new & 0x7F)
                lst[-1] <<= 7
                new = code[0]
                code = code[1:]
            lst[-1] |= new
        return code, cls(lst)
