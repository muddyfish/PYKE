
from nodes import Node
from type.type_infinite_list import DummyList

class Map(Node):
    char = "m"
    args = 0
    results = None
    contents = 1000
    
    def __init__(self, node: Node.NodeSingle):
        self.node = node
        self.args = node.args
        
    def prepare(self, stack):
        if len(stack) == 0:
            self.add_arg(stack)
        self.node.prepare(stack)
        self.args = self.node.args
        if isinstance(stack[0], dict):
            self.args = max(1, self.args-2)
    
    @Node.test_func([[-4, 2, 3, 4], 5], [[1, 7, 8, 9]], "+")
    @Node.test_func([[1, 2, 3, 4], 2], [[2, 4, 8, 16]], "^")
    @Node.test_func([[1, 0, "", "hi"]], [[0, 1, 1, 0]], "!")
    def seq_map(self, seq: Node.sequence, *args):
        end = []
        for i in seq:
            stack = [i, *args]
            self.node.prepare(stack)
            rtn = self.node(stack)
            if len(rtn) == 1:
                rtn = rtn[0]
            end.append(rtn)
        return [type(seq)(end)]
    
    @Node.test_func([5, 2], [[2, 3, 4, 5, 6]], "+")
    def int_map(self, num: int, *args):
        seq = list(range(num))
        return self.seq_map(seq, *args)

    @Node.test_func(["seed", " "], [" s e e d"], "+")
    def str_map(self, s: str, *args):
        rtn = self.seq_map(list(s), *args)[0]
        try:
            return ["".join(rtn)]
        except TypeError:
            return [rtn]
    
    @Node.test_func([{1: 3, 2: 3, 3: 4}], [{1: 3, 2: 6, 3: 12}], "*")
    @Node.test_func([{1: 3, 2: 3, 3: 4}], [{1: 4, 2: 4, 3: 5}], "h")
    def dict_map(self, dic:dict, *args):
        rtn = {}
        for key in dic:
            rtn[key] = self.node([dic[key], key, *args][:self.node.args])[0]
        return [rtn]

    def infinity_map(self, inf: Node.infinite, *args):
        return inf.modify(inf.node_map, [self.node, *args])

    def infinity_map_2(self, inf_1: Node.infinite, inf_2: Node.infinite):
        def iterate():
            while 1:
                rtn = self.node([next(inf_1), next(inf_2)])
                if len(rtn) == 1: yield rtn[0]
                else: yield rtn
        return DummyList(iterate())

    @Node.prefer
    def infinity_map_3(self, arg, inf: Node.infinite):
        return inf.modify(inf.node_left_map, [self.node, arg])
