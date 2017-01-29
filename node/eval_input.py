#!/usr/bin/env python

import copy

import __main__

import eval as safe_eval
import settings
from nodes import Node


class EvalInput(Node):
    char = "Q"
    args = 0
    results = 1
    msg = ["Q:", ""][settings.IS_WEB]
    if "web" not in __main__.__file__:
        new = safe_eval.evals[settings.SAFE](input(msg))
        contents = new
            
    def func(self):
        """Prompt for content at start. Returns by default."""
        return [copy.deepcopy(EvalInput.contents)]