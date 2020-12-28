# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла и определяет, сколько в нем слов,
# состоящих из не менее чем семи букв.

if __name__ == '__main__':
    with open('text.txt', 'r', encoding="utf8") as f:
        text = f.read()

    text = text.replace(".", " ")
    text = text.replace(",", " ")
    text = text.replace(";", " ")
    text = text.replace("!", " ")
    text = text.replace("?", " ")
    sentences = text.split(" ")

    for i in text:
        text.replace(i, ' ')
    sentences = [i for i in sentences if len(i) > 6]
    print(f'{sentences}')
    print(f'Слова, состоящие из 7 букв: {len(sentences)}')

