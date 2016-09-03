#!/usr/bin/env python

import settings
from nodes import Node

class Input(Node):
    char = "z"
    args = 0
    results = 1
    contents = ""
    def func(self):
        """input() or Input.contents"""
        msg = "z: "
        if settings.IS_WEB: msg = ""
        return input(msg) or Input.contents