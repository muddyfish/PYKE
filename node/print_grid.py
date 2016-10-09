#!/usr/bin/env python

from nodes import Node

class PrintGrid(Node):
    char = ".X"
    args = 1
    results = 1

    def __init__(self, surround: Node.StringLiteral):
        self.surround = surround

    def print_grid(self, arg: str):
        """Surround some text with characters:
0: upper (all),
1: tl (corners)
2: left
3: right
4: lower
5: tr
6: br
7: bl"""
        if self.surround == "":
            self.surround = " "
        lines = arg.splitlines()
        max_len = max(map(len, lines), default=0)
        lines = [self.surround[0]+line.ljust(max_len, " ")+self.surround[0] for line in lines]
        lines.append(self.surround[0]*(max_len+2))
        lines.insert(0, self.surround[0]*(max_len+2))
        if len(self.surround) >= 2:
            lines[0] = self.surround[1]+lines[0][1:-1]+self.surround[1]
            lines[-1] = self.surround[1]+lines[-1][1:-1]+self.surround[1]
        if len(self.surround) >= 3:
            lines = [lines[0]]+[self.surround[2]+line[1:]for line in lines[1:-1]]+[lines[-1]]
        if len(self.surround) >= 4:
            lines = [lines[0]]+[line[:-1]+self.surround[3]for line in lines[1:-1]]+[lines[-1]]
        if len(self.surround) >= 5:
            lines[-1] = lines[-1][0] + self.surround[4]*max_len + lines[-1][0]
        if len(self.surround) >= 6:
            lines[0] = lines[0][:-1]+self.surround[5]
        if len(self.surround) >= 7:
            lines[-1] = lines[-1][:-1]+self.surround[6]
        if len(self.surround) >= 8:
            lines[-1] = self.surround[7]+lines[-1][1:]
        return "\n".join(lines)
