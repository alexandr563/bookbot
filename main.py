def get_book_text(path_to_book):
    with open(path_to_book) as f:
        text_of_book = f.read()
    return text_of_book

def words_counter(text):
    list_of_words = text.split()
    count_of_words = len(list_of_words)
    print(f"{count_of_words} words found in the document")

def main():
    words_counter(get_book_text('books/frankenstein.txt'))

main()