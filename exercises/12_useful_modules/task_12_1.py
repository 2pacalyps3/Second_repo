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

def ping_ip_addresses(args):
    a = []
    b = []
    for i in args:
        result = subprocess.run(["ping", "-c", "1", "-n", i])
        if result.returncode == 0:
            a.append(i)
        else:
            b.append(i)
        d = (a, b) 
    return d


if __name__ == "__main__":
    print(ping_ip_addresses(['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128', '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']))

