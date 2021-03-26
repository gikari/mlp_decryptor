#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Шифр Гладина - шифр, которым зашифрованы многие скрытые сообщения в его пупах (которые он выпускает под ником Multiprogramm).
# В шифре присутствуют только латинские буквы, регистр не важен. В зашифрованном виде они будут представлять трёхзначное число.

def decryptChar (_dict, _val):
    for k, v in _dict.items():
        if v == _val:
            return k
    return _val

crypt = {
    'A': '394',
    'B': '110',
    'C': '321',
    'D': '846',
    'E': '271',
    'F': '730',
    'G': '981',
    'H': '401',
    'I': '237',
    'J': '903',
    'K': '845',
    'L': '101',
    'M': '902',
    'N': '900',
    'O': '197',
    'P': '314',
    'Q': '333',
    'R': '111',
    'S': '205',
    'T': '414',
    'U': '722',
    'V': '100',
    'W': '177',
    'X': '911',
    'Y': '448',
    'Z': '999'
}

def cryptString(string):
    string = string.upper()
    encrypted = ''
    for char in string:
        encrypted += crypt.get(char, char);
    return encrypted

def decryptString(string):
    string = string.upper()
    decrypted = ''
    while string[:3] != '':
        if string[:3].isdigit():
            decrypted += decryptChar(crypt, string[:3])
            string = string[3:]
        else:
            decrypted += string[0]
            string = string[1:]
    return decrypted

print ('Эта программа шифрует и дешифрует текст т. н. шифром Гладина.')
print ('Выбрать первое действие (шифровка) можно, написав число 1. Второе (дешифровка) - написав число 2.')
print ('Выберите нужное действие.')

choice = int(input())
if (choice == 1):
    print('Введите фразу, требующую шифровки.')
    S = input()
    encrypted = cryptString(S)
    print('Фраза зашифрована. Результат: ', encrypted)
elif (choice == 2):
    print('Введите зашифрованную фразу, требующую расшифровки.')
    S = input()
    decrypted = decryptString(S)
    print('Фраза расшифрована. Результат: ', decrypted)
else:
    print('Неверный ввод')
if __name__ == '__main__':
    decryptChar()
