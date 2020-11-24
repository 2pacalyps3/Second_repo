# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re



def convert_ios_nat_to_asa(filename1, filename2):
    f2 = open(filename2, "w")
    with open(filename1) as f:
        for line in f:
            match = re.search(r'ip (\S+) \w+ \w+ (\w+) (\w+) (\S+) (\d+) (\w+) \S+ (\d+)', line)
            a = "object network LOCAL_" + match[4]
            b = " host" + " " + match[4]
            c = " " + match[1] + " " + "(inside,outside) " + match[2] + " " + match[6] + " service " + match[3] + " " + match[5] + " " + match[7]
            f2.write(a + "\n")
            f2.write(b + "\n")
            f2.write(c + "\n")
convert_ios_nat_to_asa("cisco_nat_config.txt", "vyvod.txt")



