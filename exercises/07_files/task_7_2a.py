#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


from sys import argv

ignore = ["duplex", "alias", "Current configuration"]
a = argv[1]
f = open(a)

f1 = f.read().strip().split("\n")

for b in range(len(f1)):
    c = f1[b].startswith("!")
    if c == False:
        if ignore[0] in f1[b] or ignore[1] in f1[b] or ignore[2] in f1[b]:
            pass
        else:
            print(f1[b])

