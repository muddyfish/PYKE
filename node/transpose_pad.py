#!/usr/bin/env python

from nodes import Node

class PadTranspose(Node):
    char = ".,"
    args = 1
    results = 1
    contents = 0
    
    @Node.test_func([[[1,2,3],[4,5,6]]], [[[1,4],[2,5],[3,6]]])
    @Node.test_func([[[1,2,3],[4,5],[6]]], [[[1,4,6],[2,5,0],[3,0,0]]])
    def transpose(self, inp: Node.sequence):
        """Transpose with padding - contents is fill"""
        max_len = max(map(len, inp))
        rtn = []
        for i in range(max_len):
            tmp = []
            for j in range(len(inp)):
                try:
                    tmp.append(inp[j][i])
                except IndexError:
                    tmp.append(PadTranspose.contents)
            rtn.append(tmp)
        return [rtn]