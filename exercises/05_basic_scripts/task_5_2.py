# -*- coding: utf-8 -*-

"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_mask = input("Введите IP и маску: ")
ip_add = ip_mask.split("/")
mask = ip_add[-1]
add = ip_add[0]
add1 = ip_add[0].split(".")
Ip_address = """
Network:
{0:<10} {1:<10} {2:<10} {3:<10}
{0:08b}   {1:08b}   {2:08b}   {3:08b}

Mask:
/{8}
{4:<10} {5:<10} {6:<10} {7:<10}
{4:08b}   {5:08b}   {6:08b}   {7:08b}
"""
Mask1 = 32-int(mask)
Mask = "1" * int(mask) + "0" * Mask1
int1 = Mask[0:8]
int2 = Mask[8:16]
int3 = Mask[16:24]
int4 = Mask[24:32]
print(Ip_address.format(int(add1[0]), int(add1[1]), int(add1[2]), int(add1[3]), int(int1, 2), int(int2, 2), int(int3, 2), int(int4, 2), mask))

