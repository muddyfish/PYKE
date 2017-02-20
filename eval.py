#!/usr/bin/env python
import ast
import sys

from type.type_time import time_eval


def safe_eval(string):
    try:
        return ast.literal_eval(string)
    except (ValueError, SyntaxError):
        time_literal = time_eval(string)
        if time_literal:
            return time_literal
        sys.stderr.write("BAD EVAL\n")
        return string


def nonsafe_eval(string):
    try:
        return eval(string)
    except (ValueError, SyntaxError):
        time_literal = time_eval(string)
        if time_literal:
            return time_literal
        sys.stderr.write("BAD EVAL\n")
        return string

evals = {True: safe_eval, False: nonsafe_eval}
