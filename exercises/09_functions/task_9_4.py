# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]

def ignore_command(command):
    return any(word in command for word in ignore)
result = {}

def func(config_filename):
    with open(config_filename) as f:
        for line in f:       
            if line[0].isalpha() or line[0].startswith(" "):
                if ignore[0] in line or ignore[1] in line or ignore[2] in line:
                    pass
                else:     
                    a = line.rstrip()
                    if a[0].isalpha() and a.startswith(""):
                        result1 = []
                        res = a
                        result[res] = result1
                    elif a.startswith(" "):
                        res1 = a
                        result1.append(res1)
                        result[res] = result1
                        
    print(result)
func("config_sw1.txt")
print(ignore_command(result))
