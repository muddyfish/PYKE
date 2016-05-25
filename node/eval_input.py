#!/usr/bin/env python

from nodes import Node
import eval as safe_eval
import settings

import copy

class EvalInput(Node):
    char = "Q"
    args = 0
    results = 1
    
    def __init__(self):
        if not hasattr(EvalInput, "contents"):
            msg = "Q:"
            if settings.IS_WEB: msg = ""
            new = safe_eval.evals[settings.SAFE](input(msg))
            EvalInput.contents = new
            
    def func(self):
        """Prompt for content at start. Returns by default."""
        return [copy.deepcopy(EvalInput.contents)]