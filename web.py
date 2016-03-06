#!/usr/bin/env python

from flask import Flask, request, redirect, render_template
app = Flask(__name__, template_folder="web_content/template/")

@app.route("/")
def root():
    print("Hello!")
    return render_template("index.html")

@app.route("/docs")
def docs():
    return get_docs()

def get_docs():
    pass

def main(debug = True, url = "127.0.0.1"):
    app.debug = debug
    app.run(url)

if __name__ == '__main__':
    main()