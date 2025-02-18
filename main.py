def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_words_text(text)
    dict_char = get_characters_count(text)
    list_char = get_aggregated_words(text)
    print(list_char)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_words_text(words):
    word_count = len(words.split())
    return word_count

def get_characters_count(char):
    dict_char = {}
    lower_char_text = char.lower()
    for i in lower_char_text:
        if i in dict_char:
            dict_char[i] += 1
        else:
            dict_char[i] = 1
    return dict_char

def sort_on(val):
    return val["count"]

def get_aggregated_words(aggr):
    dict_char = {}
    lower_char_text = aggr.lower()
    for i in lower_char_text:
        if i.isalpha():
            if i in dict_char:
                dict_char[i] += 1
            else:   
                dict_char[i] = 1
    list_char = [{"char": key,"count": value} for key, value in dict_char.items()]
    list_char.sort(reverse=True, key=sort_on)
    return list_char


if __name__ == "__main__":
    main()

