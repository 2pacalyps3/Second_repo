# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
interface = input("Введите режим интерфейса (access/trunk) : ")
type_int = input("Введите тип и номер : ")
access_1 = "\n".join(access_template)
trunk_1 = "\n".join(trunk_template)
ans = {"access": "Введите номер VLAN: ", "trunk": "Введите номер VLANОв: "}
mode = {"access": access_1, "trunk": trunk_1}
numb = input(ans[interface])
print('interface Fa'+type_int)
print(str(mode[interface]).format(numb))


