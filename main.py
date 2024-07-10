def main():
    book_path = "/home/firsst/workspace/github.com/Firsst1/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = count_characters(text)


    report(book_path, num_words, chars_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(raw_text):
    words = raw_text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def count_characters(raw_text):
    string_dir = {}
    for s in raw_text:
        lowered = s.lower()
        if lowered.isalpha():
            if lowered in string_dir:
                string_dir[lowered] += 1
            else: 
                string_dir[lowered] = 1
    return string_dir

def sort_on(dict):
    return dict["num"]

def report(path, words, chars):

    chars_list = [{"char": key, "num": value} for key, value in chars.items()]
    chars_list.sort(reverse=True, key=sort_on)

    print(" --- Begin report of " + path + " --- ")
    print(words)
    print("")
    
    for item in chars_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

main()