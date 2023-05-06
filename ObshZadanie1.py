#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # ввод строки с клавиатуры
    string = input("Введите строку: ")

    # множество гласных букв
    vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}

    # подсчет количества гласных
    count = 0
    for char in string:
        if char in vowels:
            count += 1

    # вывод результата
    print("Количество гласных: ", count)