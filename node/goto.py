#!/usr/bin/env python

from nodes import Node
import lang_ast

class Goto(Node):
    char = "r"
    args = 0
    
    def prepare(self, stack):
        raise lang_ast.GotoStart(stack)
    
    @Node.is_func
    def goto_start(self):
        """Goto the start of the program, keeping the same stack"""
        pass
    
    @Node.is_func
    def func_return(self):
        """If in a function, return the current stack"""
        pass