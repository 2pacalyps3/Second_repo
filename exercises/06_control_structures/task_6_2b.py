# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
a = input("Enter IP: " )
b = a.split(".")

while True:
    if len(b)==4 and b[0].isdigit() and b[1].isdigit() and b[2].isdigit()and b[3].isdigit() and 0<=int(b[0])<=255  and 0<=int(b[1])<=255 and 0<=int(b[2])<=255 and 0<=int(b[3])<=255:
        if 1 <= int(b[0]) <= 223:
            print("unicast")
        elif 224 <= int(b[0]) <= 239:
            print("multicast")
        elif a == "255.255.255.255":
            print("local broadcast")
        elif a == "0.0.0.0":
            print("unassigned")
        else:
            print("unused")
        break

    a = input("Enter IP address again: " )
    b = a.split(".")

