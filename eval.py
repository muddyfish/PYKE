#!/usr/bin/env python
import ast
import settings

def safe_eval(string):
    try:
        return ast.literal_eval(string)
    except (ValueError, SyntaxError):
        if settings.WARNINGS: print("BAD EVAL")
        return string

def nonsafe_eval(string):
    try:
        return eval(string)
    except (ValueError, SyntaxError):
        if settings.WARNINGS: print("BAD EVAL")
        return string

evals = {True: nonsafe_eval, False: safe_eval}