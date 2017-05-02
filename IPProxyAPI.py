#!/usr/bin/env python3
# coding: utf-8
# File: IPProxyAPI.py
# Author: lxw
# Date: 5/2/17 3:05 PM

from flask import Flask

from redis_IP_proxy.proxy_interface import RedisClient


app = Flask(__name__)


@app.route("/")
def getIPProxy():
    client = RedisClient()
    proxy_list = client.get()
    if proxy_list:
        return proxy_list[0]
    else:
        return "No IP proxy available"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=60001)
