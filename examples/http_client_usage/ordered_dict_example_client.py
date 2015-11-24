#!/usr/bin/env python
# coding: utf-8


from __future__ import unicode_literals
from __future__ import print_function
import pyjsonrpc
import collections


# BEGIN --- required only for testing, remove in real world code --- BEGIN
import os
import sys
THISDIR = os.path.dirname(os.path.abspath(__file__))
APPDIR = os.path.abspath(os.path.join(THISDIR, os.path.pardir, os.path.pardir))
sys.path.insert(0, APPDIR)
# END --- required only for testing, remove in real world code --- END


rpc_client = pyjsonrpc.HttpClient("http://localhost:8080", gzipped=True)


print(u"UNORDERED")
print(rpc_client.call("format_text", dict([
    ("a", "AAA"),
    ("b", "BBB"),
    ("c", "CCC"),
    ("d", "DDD"),
    ("e", "EEE"),
    ("f", "FFF"),
    ("g", "GGG")
])))


print(u"ORDERED")
print(rpc_client.call("format_text", collections.OrderedDict([
    ("a", "AAA"),
    ("b", "BBB"),
    ("c", "CCC"),
    ("d", "DDD"),
    ("e", "EEE"),
    ("f", "FFF"),
    ("g", "GGG")
])))
