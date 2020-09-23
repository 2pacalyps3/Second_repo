#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv


ip_add = argv[1]
add1 = ip_add.split(".")
Ip_address = """
Network:
{0:<10} {1:<10} {2:<10} {3:<10}
{0:<08b}   {1:<08b}   {2:<08b}   {3:<08b}

Mask:
/{8}
{4:<10} {5:<10} {6:<10} {7:<10}
{4:08b}   {5:08b}   {6:08b}   {7:08b}
"""
mask = int(argv[2])
Mask1 = 32-mask
Mask = "1" * mask + "0" * Mask1
int1 = Mask[0:8]
int2 = Mask[8:16]
int3 = Mask[16:24]
int4 = Mask[24:32]
print(Ip_address.format(int(add1[0]), int(add1[1]), int(add1[2]), 0, int(int1, 2), int(int2, 2), int(int3, 2), int(int4, 2), mask))

