#!/usr/bin/env python

import lang_ast
import sys


if sys.argv[1] == "nodes":
    import nodes
    print("".join(sorted(node.char for node in nodes.nodes.values())))
    chars = {}
    for node in nodes.nodes.values():
        if node.char in chars:
            if node.char == "": continue
            print("DUPLICATE CHARS: %r and %r"%(chars[node.char], node))
        else:
            chars[node.char] = node
    sys.exit()
code = " ".join(sys.argv[1:])
print("RUNNING: %r"%code)
ast = lang_ast.AST()
ast.setup(code)
stack = ast.run()
print("STACK")
for obj in stack[::-1]:
    print(obj)