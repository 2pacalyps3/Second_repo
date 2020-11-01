# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    result0 = {}
    result1 = {}
    result2 = (result0, result1)
    with open(config_filename) as f:
        for line in f:
            if "interface" in line:
                interface = line.split()[-1]
            elif "access vlan" in line:
                vlan = line.split()[-1]
                result0[interface] = vlan
            elif "allowed vlan" in line:
                vlans1 = line.split()
                vlans = vlans1[-1].split(",")
                result1[interface] = vlans
            elif "access" in line and "vlan" not in line:
                result0[interface] = "1"
    return result2
print(get_int_vlan_map("config_sw2.txt"))

