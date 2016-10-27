
from nodes import Node
from node.map import Map

class LeftMap(Node):
    char = "L"
    args = 0
    results = None
    contents = -1
    
    def __init__(self, node:Node.NodeSingle):
        self.node = node
        self.args = node.args
        self.normal_map = Map(node)
        
    def prepare(self, stack):
        if len(stack) == 0:
            self.add_arg(stack)
        if isinstance(stack[0], dict):
            self.args = max(1, self.args-2)
        
    @Node.test_func([[10,12,23,44], 10], [[0,2,3,4]], "%")
    def seq_map(self, seq:Node.sequence, *args):
        """Map with the seq arg going on the stack last"""
        end = []
        for i in seq:
            rtn = self.node(list(args[::-1])+[i])
            if len(rtn) == 1: rtn = rtn[0]
            end.append(rtn)
        rtn = [type(seq)(end)]
        try:
            reverse_args = rtn == self.normal_map.seq_map(seq, *args)
        except:
            reverse_args = True
        if reverse_args:
            end = []
            for i in seq:
                stack = [*args, i]
                self.node.prepare(stack)
                rtn = self.node(stack)
                if len(rtn) == 1: rtn = rtn[0]
                end.append(rtn)
            return [type(seq)(end)]
        return rtn
    
    @Node.test_func([5, 2], [[2,3,4,5,6]], "+")
    def int_map(self, num:int, *args):
        """seq_map(range(num), args)"""
        seq = list(range(num))
        return self.seq_map(seq, *args)

    @Node.test_func(["seed", " "], ["s e e d "], "+")
    def str_map(self, s:str, *args):
        """seq_map(list(s), args)"""
        rtn = self.seq_map(list(s), *args)[0]
        try:
            return ["".join(rtn)]
        except TypeError:
            return [rtn]
    
    @Node.test_func([{1:3,2:3,3:4}], [{1:3,2:6,3:12}], "*")
    @Node.test_func([{1:3,2:3,3:4}], [{1:4,2:4,3:5}], "h")
    def dict_map(self, dic:dict, *args):
        """Map the values in the dictionary to node(value, key, *args)"""
        rtn = {}
        for key in dic:
            rtn[key] = self.node([dic[key], key, *args][:self.node.args])[0]
        return [rtn]