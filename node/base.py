#!/usr/bin/env python

from nodes import Node

@Node.test("b2", [5], ["101"])
@Node.test("b2", ["101"], [5])
@Node.test("b", ["  101  "], [101])
@Node.test("b2", [[2,1,0]], [10])
@Node.test("b0", [10.1], [10])
@Node.test("b0", [9.5], [10])
@Node.test("b2", [913.567], [913.57])
@Node.test("b02", [913.567], [900])
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
    
    def str_int(self, a: str):
        num = 0
        for i,char in enumerate(a[::-1]):
            num += self.base**i*self.contents.index(char)
        return num
    
    def seq_int(self, a: Node.sequence):
        result = 0
        for i, value in enumerate(a[::-1]):
            result += value*(self.base**i)
        return result
    
    def int_str(self, a: int):
        if a == 0: return self.contents[0]
        sign = "-"*(a<0)
        a = abs(a)
        digits = []
        while a:
            digits.append(self.contents[a%self.base])
            a //= self.base
        return sign+''.join(digits[::-1])
    
    def round(self, a: float):
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
        