from typing import List

from lang_ast import AST
from nodes import Node, nodes


class Explainer(object):
    def __init__(self, code: str, arg_types: List[type], indent: int=0, remaining: int=0):
        self.code = code
        self.arg_types = arg_types
        self.indent = indent
        if remaining == 0:
            remaining = self.code.count(b"\n")
        self.remaining = remaining
        self.tokens = self.parse_code(self.code)

    def __str__(self):
        rtn = self.to_str(self.tokens).split("\n")
        max_len = max(len(line) for line in rtn)
        return "\n".join("{} - ".format(line.ljust(max_len)) for line in rtn)

    def to_str(self, tokens, indent=0):
        rtn = []
        for i in tokens:
            line = i["char"]
            extend = ""
            for arg in i["args"]:
                if isinstance(arg, list):
                    if len(arg) == 1:
                        line += arg[0]["char"]
                    else:
                        new = self.to_str(arg, indent+len(line))
                        line += new.replace(" ", "").replace("\n", "")
                        if new[-1] in "()":
                            new = new[:-1].rstrip()
                        extend = "\n{}".format(new)
                else:
                    line += arg
            rtn.append(" "*indent+line+extend)
            indent += len(line)
        return "\n".join(rtn)

    def parse_code(self, code):
        rtn = []
        while code:
            new = {}
            new_code, node = AST._add_node(code)
            diff = code[:-len(new_code)]
            if diff == b"":
                diff = code
            if diff.startswith(b"."):
                if not node.ignore_dot:
                    new["char"] = diff[:2].decode("ascii")
                    diff = diff[2:]
            else:
                new["char"] = diff[:1].decode("ascii")
                diff = diff[1:]
            func = node.__init__
            annotations = func.__annotations__
            arg_names = func.__code__.co_varnames[1:func.__code__.co_argcount]
            new["args"] = []
            for arg in arg_names:
                if arg in annotations:
                    const_arg = annotations[arg]
                    arg_node = nodes[const_arg]
                    new_diff, results = node.add_const_arg(diff[:], arg_node, const_arg)
                    if new_diff is None:
                        continue
                    if len(new_diff) != 0:
                        diff = diff[:-len(new_diff)]
                    if annotations[arg] in (Node.EvalLiteral, Node.NodeSingle, Node.NodeClass):
                        new["args"].append(self.parse_code(diff))
                    else:
                        new["args"].append(diff.decode("utf-8"))
                    diff = new_diff
            code = new_code
            rtn.append(new)
        return rtn


def optimise(code):
    rtn = bytearray()
    while code:
        new_code, node = AST._add_node(code)
        diff = code[:-len(new_code)]
        if diff == b"":
            diff = code
        if diff.startswith(b"."):
            if not node.ignore_dot:
                diff[1] |= 0x80
                rtn.append(diff[1])
                diff = diff[2:]
        else:
            rtn.append(diff[0])
            diff = diff[1:]
        func = node.__init__
        annotations = func.__annotations__
        node_types = annotations.values()
        arg_names = func.__code__.co_varnames[1:func.__code__.co_argcount]
        if Node.EvalLiteral in node_types or\
           Node.NodeSingle in node_types or\
           Node.NodeClass in node_types:
            for arg in arg_names:
                if arg in annotations:
                    const_arg = annotations[arg]
                    arg_node = nodes[const_arg]
                    new_diff, results = node.add_const_arg(diff[:], arg_node, const_arg)
                    if len(new_diff) != 0:
                        diff = diff[:-len(new_diff)]
                    if annotations[arg] in (Node.EvalLiteral, Node.NodeSingle, Node.NodeClass):
                        rtn.extend(optimise(diff))
                    else:
                        rtn.extend(diff)
                    diff = new_diff
        else:
            rtn.extend(diff)
        code = new_code
    return rtn


if __name__ == '__main__':
    e = Explainer("hF1_P\n(P", arg_types=[int])
    print(e)
