#!/usr/bin/env python

from nodes import Node

class BitXOR(Node):
    args = 2
    results = 1
    char = ".^"
    
    def prepare(self, stack):
        if len(stack) == 0:
            self.add_arg(stack)
        if isinstance(stack[0], Node.sequence):
                self.args = 1
            
    @Node.test_func([4,5], [1])
    def func(self, a:int,b:int):
        """a^b"""
        return a^b

    @Node.test_func(["Test.", "Te"], [1])
    @Node.test_func(["Test.", "?"], [0])
    @Node.test_func(["Test.", "T"], [1])
    def startswith(self, string:str, suffix:str):
        """Does string start with suffix?"""
        return int(string.startswith(suffix))
    
    def xor_seq(self, seqs:Node.sequence):
        """Setwise xor of sequences"""
        if len(seqs)==0: return seqs
        rtn = []
        for seq in seqs:
            if isinstance(seq, Node.sequence):
                for i in seq:
                    if i not in rtn:
                        rtn.append(i)
                    else:
                        rtn.remove(i)
            else:
                if seq not in rtn:
                    rtn.append(seq)
                else:
                    rtn.remove(seq)
        return [rtn]
