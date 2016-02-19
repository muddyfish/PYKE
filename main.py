#!/usr/bin/env python

import lang_ast
import sys

code = " ".join(sys.argv[1:])
print "RUNNING: %r"%code
lang_ast.AST(code).run()