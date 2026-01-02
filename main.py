import sys
from stats import word_count, character_count, sort_char_list

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_contents = f.read()
            return file_contents
    except Exception:
        raise Exception

def main():
    
    #check for arguments
    if len(sys.argv) == 2:
        book_location = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(book_location)
    num_words = word_count(book_text)
    num_chars = sort_char_list(character_count(book_text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for n in num_chars:
        char = n["char"]
        num = n["num"]
        print(f"{char}: {num}")

main()