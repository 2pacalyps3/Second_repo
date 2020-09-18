# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28  в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

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
{0:<08b}   {1:<08b}   {2:<08b}   {3:<08b}

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
print(Ip_address.format(int(add1[0]), int(add1[1]), int(add1[2]), 0 , int(int1, 2), int(int2, 2), int(int3, 2), int(int4, 2), mask))

