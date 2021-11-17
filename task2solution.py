#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s):
# date:

import sys
# import nltk
from nltk.corpus import stopwords

count_dicts = []


def main():
    # nltk.download('stopwords')
    stopwords_flag = False
    if '--stopwords' in sys.argv:
        stopwords_flag = True
        # stopwords.words("russian")
        stopwords_list = stopwords.words("German") + stopwords.words("English") + stopwords.words("French")
        # stopwords_list.extend(['NN', 'ADV'])

    for file in sys.argv[1:3]:
        # count the frequencies in each file and add them to a list of dictionaries
        with open(file, encoding='utf-8') as f:
            file_words = f.read().split()
            counts = {}
            for word in file_words:
                if word.isalpha() and (not stopwords_flag or (stopwords_flag and not (word in stopwords_list))):
                    # current_count = counts.pop(word, 0)
                    # counts.update({word: current_count + 1})
                    current_count = counts.get(word, 0)
                    counts[word] = current_count + 1

            count_dicts.append(counts)

    key_dict1 = count_dicts[0].keys()
    key_dict2 = count_dicts[1].keys()
    key = key_dict1 & key_dict2

    # count_total = []
    # for k in key:
    #     count_total.append({'name': k, 'total': count_dicts[0][k] + count_dicts[1][k]})
    #
    # count_total_sort = sorted(count_total, key=lambda x: x.get('total'), reverse=True)

    # count the shared frequencies of words that exist in both dictionaries
    common_words = {}
    for k in key:
        common_words[k] = count_dicts[0][k] + count_dicts[1][k]

    # sort the dictionary and print the 10 most frequent words
    count_total_sort = dict(sorted(common_words.items(), key=lambda x: x[1], reverse=True))

    if len(sys.argv) == 3:
        count_top = 10
    else:
        count_top = int(sys.argv[3])

    i = 1
    # while i < count_top:
    #    print(count_total_sort[i])
    #    key = count_total_sort[i]["name"]
    #    print(f'N{i + 1} {key} --text: {count_dicts[0][key]} ---text2: {count_dicts[1][key]}')
    for key in count_total_sort.keys():
        if i > count_top:
            break
        print(f'N{i} {key} --text: {count_dicts[0][key]} ---text2: {count_dicts[1][key]}')
        i = i + 1


if __name__ == '__main__':
    main()

# cmd
# python task2solution.py SAC-Jahrbuch_1930_mul_columns.txt SAC-Jahrbuch_1931_mul_columns.txt
# python task2solution.py SAC-Jahrbuch_1930_mul_columns.txt SAC-Jahrbuch_1931_mul_columns.txt 30
# python task2solution.py SAC-Jahrbuch_1930_mul_columns.txt SAC-Jahrbuch_1931_mul_columns.txt 30 --stopwords
