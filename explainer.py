from typing import List

from lang_ast import AST
from nodes import Node, nodes


class NodeExplainer(object):
    def __init__(self, node: Node, diff: str, indent: int=0, remaining: int=0):
        self.node = node
        self.diff = diff
        self.indent = indent
        self.remaining = remaining

    def __str__(self):
        rtn = [b" "*self.indent + self.diff.replace(b"\n", rb"\n") + b" "*(self.remaining+1-self.diff.count(b"\n")) + b"- " + self.explain()]
        func = self.node.__class__.__init__
        annotations = func.__annotations__
        arg_names = func.__code__.co_varnames[1:func.__code__.co_argcount]
        arg_code = self.diff
        arg_code = arg_code[len(self.node.char):]
        self.indent += len(self.node.char)
        for arg in arg_names:
            if arg in annotations:
                const_arg = annotations[arg]
                node = nodes[const_arg]
                new_code, results = Node.add_const_arg(arg_code, node, const_arg)
                if new_code is not None:
                    diff = arg_code[:-len(new_code)]
                    if diff == b"":
                        diff = arg_code
                    if isinstance(results, (nodes["eval_literal"])):
                        rtn.append(str(Explainer(diff, [], self.indent, self.remaining+len(new_code))))
                    self.indent += len(diff)
                    arg_code = new_code
        return "\n".join(i.decode("ascii") for i in rtn)

    def explain(self):
        return b""


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
        return "\n".join(str(token) for token in self.tokens)

    def parse_code(self, code) -> List[Node]:
        rtn = []
        while code:
            if code.startswith(b"(") or code.startswith(b")"):
                self.indent += 1
                code = code[1:]
            new_code, node = AST._add_node(code)
            diff = code[:-len(new_code)]
            if diff == b"":
                diff = code
            code = new_code
            rtn.append(NodeExplainer(node, diff, self.indent, self.remaining+len(code)))
            self.indent += len(diff) + diff.count(b"\n")
            self.remaining -= diff.count(b"\n")
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
