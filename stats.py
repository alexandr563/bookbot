def words_counter(text):
    list_of_words = text.split()
    count_of_words = len(list_of_words)
    return count_of_words

def letter_count(text):
    letters_dict = {}
    text = text.lower()
    for letter in text:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

def dict_to_list_of_dict(dict1):
    def sort_on(items):
        return items["num"]
    
    list_of_dict = []
    for key in dict1:
        tempo_dict = {}
        tempo_dict["char"] = key
        tempo_dict["num"] = dict1[key]
        list_of_dict.append(tempo_dict)
    list_of_dict.sort(reverse=True, key = sort_on)
    return list_of_dict
