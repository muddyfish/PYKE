#!/usr/bin/env python

from node.generic_variable import Variable

class Zero(Variable):
    char = "Z"
    contents = 0
    documentation = "Add contents (default 0) to the stack"