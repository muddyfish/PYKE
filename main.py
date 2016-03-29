#!/usr/bin/env python

import lang_ast, settings, nodes
import sys

if sys.argv[1] == "nodes":
    print("\n".join(sorted(nodes.nodes.keys())))
    print("".join(sorted(node.char for node in nodes.nodes.values())))
    chars = {}
    for node in nodes.nodes.values():
        if node.char in chars:
            if node.char == "": continue
            print("DUPLICATE CHARS: %r and %r"%(chars[node.char], node))
        else:
            chars[node.char] = node
    print(chars[input()].__name__)
    sys.exit()

if settings.DEBUG:
    for node in nodes.nodes:
        nodes.nodes[node].run_tests()

code = " ".join(sys.argv[1:])
print("RUNNING: %r"%code)
ast = lang_ast.AST()
ast.setup(code)
stack = ast.run()
print("STACK")
for obj in stack[::-1]:
    print(obj)