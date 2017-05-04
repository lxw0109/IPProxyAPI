#!/usr/bin/env python3
# coding: utf-8
# File: proxies_spider.py
# Author: lxw
# Date: 4/26/17 3:13 PM

import sys
from scrapy import cmdline
# sys.path.append("/home/lxw/IT/projects/IPProxyAPI")
# sys.path.append("/home/lxw/IT/projects/IPProxyAPI/redis_IP_proxy/get_proxies")
sys.path.append("/usr/share/nginx/html/IPProxyAPI")
sys.path.append("/usr/share/nginx/html/IPProxyAPI/redis_IP_proxy/get_proxies")
# print(sys.path)
# from IPProxyAPI.redis_IP_proxy.proxy_interface import RedisClient  # NO
from redis_IP_proxy.proxy_interface import RedisClient


proxy_db = RedisClient()
# proxy_db.clean_proxies()
proxy_db.del_all_proxies()

cmdline.execute("scrapy crawl daili66_spider -L WARNING".split())
# cmdline.execute("scrapy crawl next_page_spider -L WARNING".split())
# cmdline.execute("scrapy crawl daili66_spider".split())
