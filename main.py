#!/usr/bin/env python

import lang_ast
import sys

code = " ".join(sys.argv[1:])
print "RUNNING: %r"%code
ast = lang_ast.AST()
ast.setup(code)
stack = ast.run()
print "STACK"
for obj in stack[::-1]:
    print obj