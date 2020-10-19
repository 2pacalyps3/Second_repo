#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv
f = open(argv[1])
f2 = open(argv[2], "w")
ignore = ["duplex", "alias", "Current configuration"]

f1 = f.read().strip().split("\n")

for i in range(len(f1)):
    if ignore[0] in f1[i] or ignore[1] in f1[i] or ignore[2] in f1[i]:
        pass
    else:
        f2.write(f1[i] + "\n")
f2.close()

