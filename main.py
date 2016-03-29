#!/usr/bin/env python

import lang_ast, settings, nodes
import sys
import argparse

def print_nodes():
    print("\n".join(sorted(nodes.nodes.keys())))
    print("".join(sorted(node.char for node in nodes.nodes.values())))
    chars = {}
    for node in nodes.nodes.values():
        if node.char in chars:
            if node.char == "": continue
            print("DUPLICATE CHARS: %r and %r"%(chars[node.char], node))
        else:
            chars[node.char] = node
    print(chars[input("Char? ")].__name__)
    sys.exit()

if settings.DEBUG:
    for node in nodes.nodes:
        nodes.nodes[node].run_tests()

parser = argparse.ArgumentParser(description='PYKE Interpreter')
parser.add_argument('-w', '--warnings', dest='warnings', action='store_const',
                   const=True, default=settings.WARNINGS,
                   help='Force warnings')
parser.add_argument('-s', '--safe', dest='safe', action='store_const',
                   const=True, default=settings.SAFE,
                   help='Force safe-eval')
parser.add_argument('--print-nodes', dest='print_nodes', action='store_true',
                   help='Print out all nodes and debug conflicts')
parser.add_argument('-c', '--code', nargs=1, dest='code', required=True,
                   help='The code to run')

args = parser.parse_args()

if args.print_nodes: print_nodes()
settings.WARNINGS = args.warnings
settings.SAFE = args.safe

code = args.code[0]
print("RUNNING: %r"%code)
ast = lang_ast.AST()
ast.setup(code)
stack = ast.run()
print("STACK")
for obj in stack[::-1]:
    print(obj)