# -*- coding: utf-8 -*-

from collections import Iterable

d = {'a': 1, 'b': 2, 'c':3}

for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

print(isinstance(d, Iterable))