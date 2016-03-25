#!/usr/bin/env python

from flask import Flask, request, redirect, render_template
import nodes
from collections import OrderedDict

app = Flask(__name__, template_folder="web_content/template/")

@app.route("/")
def root():
    print("Hello!")
    return render_template("index.html")

@app.route("/docs")
def docs():
    return get_docs()

def get_docs():
    docs = []
    for node in nodes.nodes:
        funcs = nodes.nodes[node].get_functions()
        for func in funcs:
            func_doc = {}
            if func.__name__ == "<lambda>":
                continue
            else:
                func_doc["name"] = func.__name__
            arg_types_dict = func.__annotations__
            func_arg_names = func.__code__.co_varnames[1:func.__code__.co_argcount]
            arg_types = OrderedDict()
            for arg in func_arg_names:
                if arg in arg_types_dict:
                    annotation = arg_types_dict[arg]
                    if isinstance(annotation, tuple):
                        arg_types[arg] = [i.__name__ for i in annotation]
                    else:
                        arg_types[arg] = [annotation.__name__]
                else:
                    arg_types[arg] = ["object"]
            func_doc["arg_types"] = arg_types
            func_doc["docs"] = func.__doc__
            func_doc["char"] = nodes.nodes[node].char
            docs.append(func_doc)
    return docs

def main(debug = True, url = "127.0.0.1"):
    app.debug = debug
    app.run(url)

if __name__ == '__main__':
    print(get_docs())
    #main()