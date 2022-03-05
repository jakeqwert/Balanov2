#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s):
# date:

import sys
import spacy

import re


def main():
    filename = sys.argv[1]
    if filename == '--min-words':
        count_words = int(sys.argv[2])
        filename = sys.argv[3]
    else:
        count_words = 0

    # --min-words 3


    with open(filename, encoding='utf-8') as file:
        text_file = file.read()
        # print(text_file)
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text_file)
        counts = {}
        for chunk in doc.noun_chunks:
            # print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
            # print(chunk.text, chunk.root.dep_, sep='==')
            current_count = counts.get(chunk.text, 0)
            counts[chunk.text] = current_count + 1
        # for ent in doc.ents:
        #     print(ent.text, ent.label_)

        count_total_sort = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

        for key in count_total_sort.keys():
            if (len(re.findall(r'\w+', key)) > count_words) and (count_words != 0):
                break
            print(f'{count_total_sort[key]} {key}')



if __name__ == '__main__':
    main()

# cmd
# python nc_counter.py corpus.txt
# python nc_counter.py --min-words 3 corpus.txt
