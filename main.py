#!/usr/bin/env python

import lang_ast, settings, nodes
import sys
import argparse

def print_nodes():
    import string
    print("\n".join(sorted(nodes.nodes.keys())))
    used_chars = sorted(node.char for node in nodes.nodes.values())
    used_chars += list("0123456789.()")
    printable = string.printable[:-5]
    print("".join(char*(char in used_chars)or" " for char in printable))
    print(printable)
    print("".join(char*(char not in used_chars)or" " for char in printable))    
    print(" ".join(char for char in used_chars if char not in printable and char != "\n"))
    chars = {}
    for node in nodes.nodes.values():
        if node.char in chars:
            if node.char == "": continue
            print("DUPLICATE CHARS: %r and %r"%(chars[node.char], node))
        else:
            chars[node.char] = node
    print(chars[input("Char? ")].__name__)
    sys.exit()

def run(code):  
    try:
        print("RUNNING: %r"%code)
    except UnicodeEncodeError:
        print("RUNNING BADUNICODE")
    ast = lang_ast.AST()
    ast.setup(code, first = True)
    stack = ast.run()
    return stack

if settings.DEBUG:
    for node in nodes.nodes:
        nodes.nodes[node].run_tests()

parser = argparse.ArgumentParser(description='PYKE Interpreter')
parser.add_argument('-w', '--warnings', dest='warnings', action='store_const',
                   const=True, default=False,
                   help='Force warnings')
parser.add_argument('-r', '--max-recurse', dest='recurse',
                   default="-1",
                   help='Recursion limit')
parser.add_argument('-s', '--safe', dest='safe', action='store_const',
                   const=True, default=settings.SAFE,
                   help='Force safe-eval')
parser.add_argument('-P', '--profile', dest='profile', action='store_const',
                   const=True, default=False,
                   help='Profile Pyke')
parser.add_argument('--print-nodes', dest='print_nodes', action='store_true',
                   help='Print out all nodes and debug conflicts')
parser.add_argument('code', nargs=1,
                   help='The code to run')
args = parser.parse_args()

if args.print_nodes: print_nodes()
settings.WARNINGS = args.warnings
settings.SAFE = args.safe
lang_ast.AST.MAX_RECURSE = int(args.recurse, 10)

if args.profile:
    import cProfile
    cProfile.run('stack = run(args.code[0])')
else:
    if args.code[0] == "Never gonna give you up":
        print("Never gonna let you down")
        sys.exit()
    else:
        stack = run(args.code[0])
print("STACK")
for obj in stack[::-1]:
    print(obj)