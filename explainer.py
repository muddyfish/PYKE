import lang_ast
from node.numeric_literal import NumericLiteral
from nodes import Node, nodes

class Explainer(object):
    def __init__(self):
        self.annotation_explain = {Node.EvalLiteral: self.explain_eval,
                                   Node.NodeSingle: self.explain_node,
                                   Node.NodeClass: self.explain_node}
    
    def explain(self, code, code_indent = 0, explain_indent = 0, pad_indent = 0):
        while code != "":
            code, node_code, node = self.add_node(code)
            print(" "*code_indent, node_code, " "*(len(code)+pad_indent), " - ", sep="", end="")
            self.parse_node(node_code, node, code_indent, explain_indent, pad_indent + len(code))
            code_indent += len(node_code)
    
    def add_node(self, code):
        new_code, node = lang_ast.AST._add_node(code)
        if new_code == "":
            code_removed = code
        else:                
            code_removed = code[:-len(new_code)]
        return new_code, code_removed, node

    def parse_node(self, code, node, code_indent, explain_indent, pad_indent):
        code_indent += len(node.char)
        func = node.__init__
        annotations = func.__annotations__
        if annotations:
            code = code[len(node.char):]
            arg_names = func.__code__.co_varnames[1:func.__code__.co_argcount]
            for arg_name in arg_names:
                if arg_name not in annotations: continue
                annotation_name = annotations[arg_name]
                if annotation_name in self.annotation_explain:
                    self.annotation_explain[annotation_name](code, node, code_indent, explain_indent, pad_indent)
                else:
                    annotation_class = nodes[annotation_name]
                    new_code, annotation_node = Node.add_const_arg(code, annotation_class, annotations[arg_name])
                    print(node)
        else:
            self.explain_default(code, node)
    
    def explain_eval(self, code, node, code_indent, explain_indent, pad_indent):
        print(node)
        if code[-1] in lang_ast.AST.END_CHARS:
            code = code[:-1]
            pad_indent += 1
        self.explain(code, code_indent, explain_indent, pad_indent)
        
    def explain_node(self, code, node, code_indent, explain_indent, pad_indent):
        print(node)
    
    def explain_default(self, code, node):
        print(node)
    
    def check_code(self, code, node):
        if node.accepts(code) == (None, None):
            print("Node (",node,") doesn't accept ", code, sep="")
    
        

if __name__ == '__main__':
    e = Explainer()
    e.explain("hZRVoeX*oe+")