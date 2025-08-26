def words_counter(text):
    list_of_words = text.split()
    count_of_words = len(list_of_words)
    print(f"{count_of_words} words found in the document")

def letter_count(text):
    letters_dict = {}
    text = text.lower()
    for letter in text:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict