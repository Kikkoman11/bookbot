def main():
    #Main function to generate a report of the book
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_words_text(text)
    char_count = get_characters_count(text)
    sorted_char_count = get_sorted_char_count(char_count)

    #Prints the report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")

    for char_dict in sorted_char_count:
        print(f"The '{char_dict['char']}' character was found '{char_dict['count']}' times")
    print("--- End of report ---")

def get_book_text(path):
    #Reads and returns the text of the txt file
    with open(path) as f:
        return f.read()
    
def get_words_text(text):
    #Counts the number of words in the text
    return len(text.split())

def get_characters_count(text):
    #Counts the frequency of each character in the text
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(val):
    #Fuction for sorting dictionnaries by count value
    return val["count"]

def get_sorted_char_count(char_count):
    #Creates a list of dictionnaries for alphabetical characters
    list_char = [
        {"char": char,"count": count}
        for char, count in char_count.items()
        if  char.isalpha()]
    list_char.sort(reverse=True, key=sort_on)
    return list_char


if __name__ == "__main__":
    main()

