def get_book_text(path_to_book):
    with open(path_to_book) as f:
        text_of_book = f.read()
    print(text_of_book)
    pass

def main():
    get_book_text('books/frankenstein.txt')

main()