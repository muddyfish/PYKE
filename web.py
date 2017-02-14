#!/usr/bin/env python

import os
import signal
import subprocess
import sys
from collections import OrderedDict
from io import StringIO
from subprocess import Popen, PIPE, STDOUT, TimeoutExpired

from flask import Flask, request, redirect, render_template, send_from_directory
from flask.ext.cache import Cache

import explainer
import lang_ast
import literal_gen
import nodes
import settings

for node in nodes.nodes:
    nodes.nodes[node].run_tests()

is_windows = hasattr(os.sys, 'winver')

sys.stdin = StringIO()
app = Flask(__name__,
            template_folder="web_content/template/",
            static_folder="web_content/static/")
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

modified_process = Popen(["git",
                          "log",
                          "-1",
                          "--format=%cd",
                          "--date=local"],
                         stdout=PIPE)
output, errors = modified_process.communicate()
updated_time = output.decode()[:-1]
if is_windows:
    updated_time += ", WINDOWS"


@app.route("/")
def root():
    code = request.args.get("code", "")
    inp = request.args.get("input", "")
    warnings = int(request.args.get("warnings", "1"))
    return render_template("index.html",
                           last_updated=updated_time,
                           docs=docs(),
                           code=code,
                           input=inp,
                           warnings=warnings)


@app.route("/code")
@app.route("/blog")
def rick():
    return redirect("http://www.youtube.com/watch?v=dQw4w9WgXcQ")


@app.route("/submit", methods=['POST'])
def submit_code(timeout=5):
    code = request.form.get("code", "")
    inp = request.form.get("input", "") + "\n"
    print(code, inp)
    warnings = int(request.form.get("warnings", "0"), 10)
    args = ['python3',
            'main.py',
            '--safe',
            '--',
            code]
    stderr = PIPE
    if warnings:
        args.insert(2, "--warnings")
        stderr = STDOUT
    with Popen(args,
               stdin=PIPE,
               stdout=PIPE,
               stderr=stderr,
               creationflags=is_windows and subprocess.CREATE_NEW_PROCESS_GROUP) as process:
        process.stdin.write(bytearray(inp, "utf-8"))
        process.stdin.close()
        response = ""
        try:
            process.wait(timeout)
        except TimeoutExpired:
            response = "Timeout running code.\n"
            if is_windows:
                os.kill(process.pid, signal.CTRL_BREAK_EVENT)
            else:
                process.send_signal(signal.SIGTERM)
            try:
                process.wait(2)
            except TimeoutExpired:
                response += "Really timed out code\n"
            process.kill()
        response += process.stdout.read().decode("cp1252", errors="replace")
    return response


@app.route("/explain", methods=['POST'])
def explain_code():
    code = request.form.get("code", "")
    try:
        return ("\n"+str(explainer.Explainer(code, []))).replace("\n", "\n    ")
    except:
        return ""


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
            if hasattr(nodes.nodes[node], "documentation"):
                func_doc["docs"] = nodes.nodes[node].documentation
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
                func_doc["output"] = func_doc["output"].replace("<", "&lt;")
                func_doc["output"] = func_doc["output"].replace(">", "&gt;")
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


def main(debug = settings.DEBUG, url="127.0.0.1"):
    app.debug = debug
    app.run(url)

if __name__ == '__main__':
    main()
