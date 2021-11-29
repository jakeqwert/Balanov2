#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s):
# date:

import sys
import nltk
from nltk.tokenize import sent_tokenize
import re


def main():
    filename = sys.argv[1]
    with open(filename, encoding='utf-8') as file:
        text_file = file.read()
        tokenize = sent_tokenize(text_file, language="english")
        for n, proposal in enumerate(tokenize[:50]):
            print(f'###N{n} = {proposal}')



if __name__ == '__main__':
    main()

# cmd
# python task2ex5solution.py dune.txt
# python task2ex5solution.py die_verwandlung.txt
# python task2ex5solution.py les_mariages_de_Paris.txt
