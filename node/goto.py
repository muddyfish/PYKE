#!/usr/bin/env python

from nodes import Node
import lang_ast

class Goto(Node):
    char = "r"
    
    def prepare(self, stack):
        """Goto the start of the program, keeping the same stack"""
        raise lang_ast.GotoStart(stack)