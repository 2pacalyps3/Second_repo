# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
def ping_ip_addresses(*args):
    a = []
    b = []
    for i in args:
        result = subprocess.run(["ping", "-c", "1", "-n", i])
        if result.returncode == 0:
            a.append(i)
        else:
            b.append(i)
        c = (a, b) 
    print(c)
    return c
    
ping_ip_addresses("a", "8.8.8.8", "1.1.1.1", "1.1.1")


