# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf1 = ospf_route.split()
ospf1.pop(2)
print("{ospf:30}".format(ospf = "Prefix") + "{route}".format(route = ospf1[0]))
print("{ospf_1:30}".format(ospf_1 = "AD/Metric") + "{route}".format(route = ospf1[1]))
print("{ospf_2:30}".format(ospf_2 = "Next-Hop") + "{route}".format(route = ospf1[2]))
print("{ospf_3:30}".format(ospf_3 = "Last update") + "{route}".format(route = ospf1[3]))
print("{ospf_4:30}".format(ospf_4 = "Outbound Interface") + "{route}".format(route = ospf1[4]))






