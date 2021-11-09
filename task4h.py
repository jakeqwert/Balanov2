#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s):
# date:

import wikipedia
import sys
import re


def main():
    list_titles = sys.argv[1].split(', ')

    # print(len(sys.argv))

    if len(sys.argv) == 3:
        lang = str(sys.argv[2])
        if lang not in wikipedia.languages().keys():
            lang = 'de'
    else:
        lang = 'de'

    wikipedia.set_lang(lang)

    for title in list_titles:
        my_summary = wikipedia.summary(title)
        my_list = re.findall('\d[\d,]* \S+', my_summary)
        print(title, my_list)


if __name__ == '__main__':
    main()

# cmd
# python task4h.py "Zurich, Geneva" en
# python task4h.py Zurich en
# python task4h.py Zurich