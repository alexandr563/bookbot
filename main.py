from stats import words_counter

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        text_of_book = f.read()
    return text_of_book

def main():
    words_counter(get_book_text('books/frankenstein.txt'))

main()