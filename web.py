#!/usr/bin/env python

from flask import Flask, request, redirect, render_template, send_from_directory
from flask.ext.cache import Cache

from collections import OrderedDict
import time
import subprocess

import nodes, lang_ast, settings
import literal_gen

for node in nodes.nodes:
    nodes.nodes[node].run_tests()
        
app = Flask(__name__,
            template_folder="web_content/template/",
            static_folder="web_content/static/")
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

modified_process = subprocess.Popen(["git",
                                     "log",
                                     "-1",
                                     "--format=%cd",
                                     "--date=local"],
    stdout=subprocess.PIPE)
output, errors = modified_process.communicate()
updated_time = output.decode()[:-1]

@app.route("/")
def root():
    code = request.args.get("code", "")
    inp = request.args.get("input", "")
    warnings = int(request.args.get("warnings", "1"))
    return render_template("index.html",
                           last_updated = updated_time,
                           docs = docs(),
                           code = code,
                           input = inp,
                           warnings = warnings)


@app.route("/code")
@app.route("/blog")
def rick():
    return redirect("http://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app.route("/submit", methods = ['POST'])
def submit_code():
    code = request.form.get("code", "")
    if code == "Never gonna give you up":
        return "Never gonna let you down"
    inp = request.form.get("input", "") + "\n"
    warnings = int(request.form.get("warnings", "0"), 10)
    max_recurse = max(1, min(10000, int(request.form.get("max_recurse", "1000"), 10)))
    args = ['python3',
            'main.py',
            '--max-recurse',
            str(max_recurse),
            '--safe',
            '--',
            code]
    stderr = subprocess.PIPE
    if warnings:
        args.insert(2, "--warnings")
        stderr = subprocess.STDOUT
    try:
        process = subprocess.check_output(args,
                                           input=bytearray(inp, 'utf-8'),
                                           stderr=stderr,
                                           timeout = 5)
        response = process.decode()
    except subprocess.CalledProcessError as e:
        response = e.output.decode()
    except subprocess.TimeoutExpired as e:
        response = "Timeout running code.\n"
        response += e.output.decode()
    return response

@app.route("/dictionary")
def dictionary():
    return render_template("dictionary.html")

@app.route("/dict_compress", methods = ['POST'])
def dict_compress():
    inp = request.form.get("compress")
    return nodes.nodes["dictionary"].compress(inp)

@app.route("/docs")
@cache.cached(timeout=3600)
def docs():
    docs = get_docs()
    keys = ["char", "name", "arg_types", "fixed_params", "input", "output", "docs"]
    types = ["<br>","<br>","<br>","<br>","<pre>","<pre>","<br>"]
    table = []
    for func in docs:
        row = [func[doc_type] for doc_type in keys]
        for i, col in enumerate(row):
            try:
                if types[i] == "<br>":
                    row[i] = col.replace("\n", "<br>")
                elif types[i] == "<pre>":
                    row[i] = '<pre class="doc_pre">'+str(col)+"</pre>"
            except AttributeError: pass
        table.append(row)
    table.sort(key = lambda x:x[0]+x[1])
    keys = [key.title().replace("_", " ") for key in keys]
    app.jinja_env.autoescape = False
    rtn = render_template("docs_table.html", keys = keys, funcs = table)
    app.jinja_env.autoescape = True
    return rtn

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
            cls_init = nodes.nodes[node].__init__
            fixed = cls_init.__annotations__
            func_doc["fixed_params"] = ""
            if fixed:
                arg_names = cls_init.__code__.co_varnames[1:cls_init.__code__.co_argcount]
                for arg in arg_names:
                    if arg in fixed:
                        func_doc["fixed_params"] += fixed[arg]+"\n"
            elif nodes.nodes[node].accepts.__module__ != "nodes":
                func_doc["fixed_params"] = "custom"
            func_doc["docs"] = func.__doc__
            func_doc["char"] = nodes.nodes[node].char
            func_doc["input"] = ""
            func_doc["output"] = ""
            if hasattr(func, "tests"):
                try:
                    nodes.nodes[node].reset_tests()
                except AttributeError:
                    pass
                for test in func.tests[::-1]:
                    try:
                        inp = literal_gen.stack_literal(test[0])
                        cmd = nodes.nodes[node].char+test[-1]
                        lang_ast.test_code(inp+cmd, test[1])
                    except NotImplementedError:
                        func_doc["input"] = "Literal Undefined\n"
                        func_doc["output"] = str(test[1])+"\n"
                    else:
                        func_doc["input"] += (inp+cmd+"\n")
                        func_doc["output"] += (str(test[1])+"\n")
                func_doc["input"] = func_doc["input"][:-1]
                func_doc["output"] = func_doc["output"][:-1]
            docs.append(func_doc)
    return docs

def print_ordered_dict(ordered):
    rtn = ""
    for key, value in ordered.items():
        rtn += key+": "+str(value).replace("'","")+"\n"
    return rtn[:-1]


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('web_content/static', path)

def main(debug = settings.DEBUG, url = "127.0.0.1"):
    app.debug = debug
    app.run(url)

if __name__ == '__main__':
    main()