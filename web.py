#!/usr/bin/env python

from flask import Flask, request, redirect, render_template
from flask.ext.cache import Cache

from collections import OrderedDict

import nodes

app = Flask(__name__, template_folder="web_content/template/")
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/docs")
@cache.cached(timeout=3600)
def docs():
    docs = get_docs()
    keys = ["char", "name", "arg_types", "fixed_params", "docs"]
    table = []
    for func in docs:
        row = [func[doc_type] for doc_type in keys]
        table.append(row)
    table.sort(key = lambda x:x[0]+x[1])
    return render_template("docs_table.html", keys = keys, funcs = table)

def get_docs():
    docs = []
    for node in nodes.nodes:
        if nodes.nodes[node].ignore: continue
        funcs = nodes.nodes[node].get_functions()
        for func in funcs:
            func_doc = {}
            if func.__name__ == "<lambda>":
                continue
            elif func.__name__ == "func":
                func_doc["name"] = node
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
            func_doc["arg_types"] = print_ordered_dict(arg_types)
            if func.__code__.co_flags & 4:
                if func_doc["arg_types"]: func_doc["arg_types"] += "\n"
                func_doc["arg_types"] += "*args"
            fixed = nodes.nodes[node].__init__.__annotations__
            if fixed:
                func_doc["fixed_params"] = tuple(fixed.values())[0]
            elif nodes.nodes[node].accepts.__module__ != "nodes":
                func_doc["fixed_params"] = "custom"
            else:
                func_doc["fixed_params"] = ""
            func_doc["docs"] = func.__doc__
            func_doc["char"] = nodes.nodes[node].char
            docs.append(func_doc)
    return docs

def print_ordered_dict(ordered):
    rtn = ""
    for key, value in ordered.items():
        rtn += key+": "+str(value).replace("'","")+"\n"
    return rtn[:-1]

def main(debug = True, url = "127.0.0.1"):
    app.debug = debug
    app.run(url)

if __name__ == '__main__':
    #print(get_docs())
    main()