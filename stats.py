def word_count(book_text):
    count = len(book_text.split())
    return count


def character_count(book_text):
    char_dict = {}
    words = book_text.split()
    for w in words:
        for c in w:
            char = c.lower()
            if char in char_dict:
                char_dict[char] +=1
            else:
                char_dict[char] = 1
    return char_dict


def sort_on(items):
    return items["num"]


def sort_char_list(char_dict):
    sorted_list = []
    for c in char_dict:
        if c.isalpha():
            num = char_dict[c]
            new_dict = {"char": c, "num": num}
            sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list