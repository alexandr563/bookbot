import sys

from stats import words_counter
from stats import letter_count
from stats import dict_to_list_of_dict

sys_arg = sys.argv
if not len(sys_arg) == 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

path = sys_arg[1]

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        text_of_book = f.read()
    return text_of_book

def main():
    letters_dictionary = letter_count(get_book_text(path)) 
    list_of_dict = dict_to_list_of_dict(letters_dictionary)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {words_counter(get_book_text(path))} total words')
    print('--------- Character Count -------')
    for i in list_of_dict:
        if i['char'].isalpha():
            char = i['char']
            num = i['num']
            print(f'{char}: {num}')
    print('============= END ===============')


main()