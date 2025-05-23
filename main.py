from stats import get_book_words
from stats import get_book_chars
from stats import sorted_list
import sys

filename = ""
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filename = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    #print(get_book_text(filename))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    num_of_words = get_book_words(filename)
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    char_count = get_book_chars(filename)
    #print(char_count)
    sorted_list_dict = sorted_list(char_count)
    #print(sorted_list_dict)
    for entry in sorted_list_dict:
        if entry["char"].isalpha():
            cur_char = entry["char"]
            cur_num = entry["num"]
            print(f"{cur_char}: {cur_num}")

main()
