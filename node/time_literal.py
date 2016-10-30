#!/usr/bin/env python

from nodes import Node
from type.type_time import TypeTime


class TimeLiteral(Node):
    char = "y"
    args = 0
    results = 1
    
    def __init__(self, time:Node.StringLiteral):
        self.time = TypeTime.parse_strtime(time)

    def func(self):
        return [self.time]
