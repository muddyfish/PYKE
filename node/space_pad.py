#!/usr/bin/env python

from nodes import Node


class SpacePad(Node):
    char = ".\\"
    args = 1
    results = 1

    def __init__(self, pad: Node.StringSingle):
        self.pad = pad

    def space_pad(self, arg: int):
        """Pad the character with `arg` spaces to the left"""
        return " "*arg + self.pad