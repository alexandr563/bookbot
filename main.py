from stats import words_counter

from stats import letter_count

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        text_of_book = f.read()
    return text_of_book

def main():
    letters_dictionary = letter_count(get_book_text('books/frankenstein.txt'))
    words_counter(get_book_text('books/frankenstein.txt'))
    print(letters_dictionary)

main()