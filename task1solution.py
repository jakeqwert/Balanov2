import os
import re
import sys
# import unicodedata

def normalize(name):
    # TODO1 function to normalize ü,ö,ä etc.
    name = name.lower()
    name = re.sub(r'[ùúûü]', 'ue', name)
    name = re.sub(r'[òóôõö]', 'oe', name)
    name = re.sub(r'[àáâãäå]', 'ae', name)
    name = re.sub(r'[èéêë]', 'ee', name)
    name = re.sub(r'[ìíîï]', 'ie', name)
    # name = unicodedata.normalize('NFD', name)
    return name


def get_consonants(name):
    # TODO1 function to return just the consonants in a given name
    name = re.sub(r'[aeiou]', '', name)
    return name


def parse_name(name):
    # TODO1 function to return first and last names according to all rules
    # parse the names to first and last names
    # Wolfgang Amadeus Mozart -> first_name = wlfgngmds, last_name = mozart
    name = normalize(name)

    # search first word
    # first_name = re.search(r'^\w+', name).group(0)

    # search last word
    last_name = re.search(r'\w+$', name).group(0)

    # search first word and middle
    first_name = re.sub(last_name, '', name)
    first_name = re.sub(r'\s', '', first_name)  # space

    if len(first_name) > 8:
        first_name = get_consonants(first_name)

    # print(name, 'first_name='+first_name+', '+'last_name='+last_name, sep=' -> ')
    return first_name, last_name


def create_email_adress(first_name, last_name, domain):
    # function to create an email address
    if domain == 'stu':
        domain = 'uzh.ch'
    else:
        domain = domain + '.uzh.ch'

    return first_name + '.' + last_name + '@' + domain


def main():
    # reading of the file/reading of the name from the command line comes here
    if len(sys.argv) == 1:  # default text file 'names.txt'
        file_name = 'names.txt'
        if not os.path.exists(file_name):
            print('file not found')
    else:
        argv = sys.argv[1]
        # TODO1 text file or single name
        if not os.path.exists(argv):  # single name
            # file not exists,
            first_name, last_name = parse_name(argv)
            print(argv, create_email_adress(first_name, last_name, 'stu'), sep=' -> ')
        else:  # text file
            # file exists
            with open(argv, encoding='utf-8') as file:
                # file_lines = file.read().splitlines()
                file_lines = re.split(r'\n', file.read())
                pattern = re.compile(r'\t')
                for line in file_lines:
                    # name, domain = re.split(r'\t', line)
                    name, domain = pattern.split(line)
                    first_name, last_name = parse_name(name)
                    print(line, create_email_adress(first_name, last_name, domain), sep=' -> ')


if __name__ == '__main__':
    main()

# cmd
# python task1solution.py names.txt
# python task1solution.py "Michael Richards"
