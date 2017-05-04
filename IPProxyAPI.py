#!/usr/bin/env python3
# coding: utf-8
# File: IPProxyAPI.py
# Author: lxw
# Date: 5/2/17 3:05 PM

from flask import Flask

from redis_IP_proxy.proxy_interface import RedisClient


app = Flask(__name__)

client = RedisClient()


@app.route("/plain")
def get_ip_proxy_plain():
    proxy_list = client.get()
    if proxy_list:
        return proxy_list[0]
    else:
        return "No IP proxy available"


@app.route("/")
def get_ip_proxy():
    return '<div style="text-align: center; "><h1>Your proxy is&nbsp;&nbsp;{}</h1></div>'.format(get_ip_proxy_plain())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=60001)
