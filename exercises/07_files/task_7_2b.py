# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]
f = open("config_sw1.txt")
f1 = f.read().strip().split("\n")
f2 = open("config_sw1_cleared.txt", "w")
for i in range(len(f1)):
    if ignore[0] in f1[i] or ignore[1] in f1[i] or ignore[2] in f1[i]:
        pass
    else:
        f2.write(f1[i] + "\n")
f2.close()
        
