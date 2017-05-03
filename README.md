# IPProxyAPI

`IPProxyAPI`: An API to provide free IP proxy.

Gathering **Free** IP proxies on the Internet, and serving as an API.

Based on [`Flask`](http://docs.jinkan.org/docs/flask/quickstart.html#quickstart) and [`Redis`](https://redis.io/).


### FAQs
1. `pip3 install cryptography` 一直出错，在网上尝试了各种各样的办法，后来参考[这里](https://github.com/pyca/cryptography/issues/3376)，考虑到可能是有些软件包太旧了，于是通过
```bash
$ sudo apt-get update
$ sudo apt-get upgrade --fix-missing
```
终于把cryptography装上了
估计是阿里云服务器上的软件版本太旧导致的
2. 
