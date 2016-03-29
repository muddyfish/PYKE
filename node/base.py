#!/usr/bin/env python

from nodes import Node

class Base(Node):
    char = "b"
    args = 1
    results = 1
    contents = "0123456789abcdefghijklmnopqrstuvwxyz"
    default_arg = 10
    
    def __init__(self, base: Node.NumericLiteral):
        self.base = base
    
    def prepare(self, stack):
        if not self.overwrote_default and self.base == 10:
            self.base = Base.default_arg

    @classmethod
    def update_contents(cls, new_var):
        cls.default_arg = len(new_var)
        cls.contents = new_var
    
    @Node.test_func(["  101  "], [101])
    @Node.test_func(["101"], [5], "2")
    def str_int(self, a: str):
        """Return a in base `base` as an integer
Base contents can be changed by changing the contents"""
        num = 0
        a = a.replace(" ","")
        mult = 0
        if "." in a:
            mult = len(a)-a.index(".")-1
        a = a.replace(".","")
        for i,char in enumerate(a[::-1]):
            num += self.base**(i-mult)*self.contents.index(char)
        return num
    
    @Node.test_func([[2,1,0]], [10], "2")
    def seq_int(self, a: Node.sequence):
        """Return a in base `base`"""
        result = 0
        for i, value in enumerate(a[::-1]):
            result += value*(self.base**i)
        return result
    
    @Node.test_func([5], ["101"], "2")
    def int_str(self, a: int):
        """Return a in base `base`
Base contents can be changed by changing the contents"""
        if a == 0: return self.contents[0]
        sign = "-"*(a<0)
        a = abs(a)
        digits = []
        while a:
            digits.append(self.contents[a%self.base])
            a //= self.base
        return sign+''.join(digits[::-1])
    
    @Node.test_func([10.1], [10], "0")
    @Node.test_func([9.5], [10], "0")
    @Node.test_func([913.567], [913.57], "2")
    @Node.test_func([913.567], [900], "02")
    def round(self, a: float):
        """round(a, `base`)"""
        mult = 1
        if isinstance(self.base, str):
            mult = -1
            self.base = int(self.base, 10)
        rtn = round(a, self.base*mult)
        if rtn%1 == 0:
            rtn = int(rtn)
        return rtn
        
    def __repr__(self):
        return "%s: %s"%(self.__class__.__name__, self.base)
        