#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s):
# date:

import sys
import re


def create_sentiment_dict(filename):
    # Todo1: implement the function
    sentiment_dict = {}
    with open(filename, encoding='utf-8') as file:
        file_lines = file.read().splitlines()
        pattern = re.compile(r'\t')
        for line in file_lines:
            adjective, sentiment = pattern.split(line)

            # if sentiment == 'positive':
            #     sentiment_dict[adjective] = 1
            # elif sentiment == 'neutral':
            #     sentiment_dict[adjective] = 0
            # elif sentiment == 'negative':
            #     sentiment_dict[adjective] = -1

            switch = {
              'positive': 1,
              'neutral':  0,
              'negative': -1,
            }.get(sentiment)
            sentiment_dict[adjective] = switch

    return sentiment_dict



def calculate_avg_sentiment(filename, sentiment_dict):
    # Todo2: implement the funcion
    with open(filename, encoding='utf-8') as file:
        file_lines = file.read().splitlines()
        pattern = re.compile(r'\t')

        counts = 0
        total_counts = 0
        for line in file_lines:
            word, poss = pattern.split(line)
            if poss == 'JJ':
                counts = counts + sentiment_dict.get(word, 0)
                total_counts = total_counts + 1
    avg = counts / total_counts
    return avg

def main():
    # Uncomment the following line to call the function to create a dictionary:
    sentiment_dict = create_sentiment_dict(sys.argv[1])
    # print(sentiment_dict)
    # Printing your results to the console:
    print(calculate_avg_sentiment(sys.argv[2], sentiment_dict))


if __name__ == '__main__':
    main()

# cmd
# python task3solution.py adjective_sentiment.txt test_hobbies.txt