#!/usr/bin/env python

import argparse
import sys

import lang_ast
import nodes
import settings


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
            if node.char == "":
                continue
            print("DUPLICATE CHARS: %r and %r"%(chars[node.char], node))
        else:
            chars[node.char] = node
    print(chars[input("Char? ")].__name__)
    sys.exit()


def run(code):  
    try:
        print("RUNNING: {} ({} bytes)".format(repr(code), len(code.encode("utf-8"))))
    except UnicodeEncodeError:
        print("RUNNING BAD UNICODE")

    ast = lang_ast.AST()
    ast.setup(code, first=True)
    stack = ast.run()
    return stack


def run_file(filename):
    with open(filename, "rb") as f_obj:
        string = ""
        for char in f_obj.read():
            string += chr(char)
        return run(string)


class Writer(type(sys.stdout)):
    auto_newline = False

    def __init__(self, *writers):
        self.writers = writers
        self.line_length = 0

    def set_auto_newline(self, length):
        self.line_length = 0
        self.auto_newline = length

    def write(self, text):
        for w in self.writers:
            for i in str(text):
                try:
                    w.write(i)
                except UnicodeEncodeError:
                    w.write("\\x" + hex(ord(i))[2:])
                self.line_length += 1
                if self.line_length == self.auto_newline:
                    self.line_length = 0
                    w.write("\n")
                elif i == "\n":
                    self.line_length = 0
                w.flush()


sys.stdout = Writer(sys.stdout)
    
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
parser.add_argument('-f', '--file', dest="file", nargs=1,
                    help='The file to look in')
parser.add_argument('code', nargs="*",
                    help='The code to run')
args = parser.parse_args()

if args.print_nodes:
    print_nodes()
settings.WARNINGS = args.warnings
settings.SAFE = args.safe
lang_ast.AST.MAX_RECURSE = int(args.recurse, 10)

if __name__ == "__main__":
    if args.file:
        f_name = args.file[0]
        run_string = 'stack = run_file(f_name)'
    else:
        run_string = 'stack = run(args.code[0])'
    run_func = exec
    if args.profile:
        import cProfile
        run_func = cProfile.run()
    run_func(run_string)
    if settings.WARNINGS:
        print("STACK")
    for obj in stack[::-1]:
        print(obj)