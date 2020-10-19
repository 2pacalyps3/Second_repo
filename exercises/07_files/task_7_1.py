# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
a = ["Prefix", "AD/Metric", "Next-Hop", "Last update", "Outbound Interface"]

f = open("ospf.txt")

f1 = f.read().replace("O", "").replace("via", "").replace("[", "").replace("]", "").replace(",", "").split("\n")

for c in f1:
    c1 = c.split()
    for i in range(len(c1)):
        print("{:25}".format(a[i]) + " " + c1[i])
