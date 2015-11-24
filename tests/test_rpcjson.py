#!/usr/bin/env python
# coding: utf-8
"""
Nosetests for *rpcjson.py*.
"""


from __future__ import unicode_literals
import pyjsonrpc.rpcjson
import json


DATA = {
    "nested_dict": {"key": "value"},
    "nested_list": [1, 2, 3, 4],
    "int": 1,
    "float": 1.1,
    "unicode": "Ünicöde",
}


def test_roundtrip():
    assert(pyjsonrpc.rpcjson.loads(pyjsonrpc.rpcjson.dumps(DATA)) == DATA)


def test_compatibility():
    encoded = pyjsonrpc.rpcjson.dumps(DATA)
    assert(encoded == json.dumps(DATA))
    decoded = pyjsonrpc.rpcjson.loads(encoded)
    assert(decoded == json.loads(encoded))
