#!/usr/bin/env python3
# coding: utf-8
# File: proxies_spider.py
# Author: lxw
# Date: 4/26/17 3:13 PM

import sys
from scrapy import cmdline

"""
sys.path.append("/home/lxw/IT/projects/IPProxyAPI/redis_IP_proxy")
print(sys.path)
"""
sys.path = ['/home/lxw/IT/projects/IPProxyAPI/redis_IP_proxy/get_proxies', '/home/lxw/IT/projects/IPProxyAPI', '/home/lxw/IT/program/LXW_VIRTUALENV/py361scrapy133/lib/python36.zip', '/home/lxw/IT/program/LXW_VIRTUALENV/py361scrapy133/lib/python3.6', '/home/lxw/IT/program/LXW_VIRTUALENV/py361scrapy133/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6', '/home/lxw/IT/program/LXW_VIRTUALENV/py361scrapy133/lib/python3.6/site-packages', '/home/lxw/.local/lib/python3.6/site-packages', '/usr/local/lib/python3.6/site-packages', '/home/lxw/IT/projects/IPProxyAPI/redis_IP_proxy']

from proxy_interface import RedisClient

proxy_db = RedisClient()
proxy_db.clean_proxies()

cmdline.execute("scrapy crawl daili66_spider -L WARNING".split())
# cmdline.execute("scrapy crawl next_page_spider -L WARNING".split())
# cmdline.execute("scrapy crawl daili66_spider".split())
