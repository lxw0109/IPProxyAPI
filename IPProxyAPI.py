#!/usr/bin/env python3
# coding: utf-8
# File: IPProxyAPI.py
# Author: lxw
# Date: 5/2/17 3:05 PM

from flask import Flask
app = Flask(__name__)

@app.route("/")
def getIPProxy():
    return "192.168.1.41"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
