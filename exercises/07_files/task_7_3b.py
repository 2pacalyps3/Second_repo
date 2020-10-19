# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
f = open("CAM_table.txt")
f1 = f.read().strip().split('\n')
vlan = input("Enter VLAN: ")
list_1 = []
for i in range(len(f1)):
    a = f1[i].startswith(" ")
    if a == True:
        b = f1[i].split()
        b.pop(2)
        if b[0].isdigit():
            b[0] = int(b[0])
            list_1.append(b)
for k in range(len(list_1)):
    if vlan == str(list_1[k][0]):
        print(list_1[k])

