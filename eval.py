#!/usr/bin/env python
import ast

import settings
from type.type_time import time_eval


def safe_eval(string):
    try:
        return ast.literal_eval(string)
    except (ValueError, SyntaxError):
        time_literal = time_eval(string)
        if time_literal:
            return time_literal
        if settings.WARNINGS: print("BAD EVAL")
        return string


def nonsafe_eval(string):
    try:
        return eval(string)
    except (ValueError, SyntaxError):
        time_literal = time_eval(string)
        if time_literal:
            return time_literal
        if settings.WARNINGS: print("BAD EVAL")
        return string

evals = {True: safe_eval, False: nonsafe_eval}
