def get_book_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        file_as_words = file_contents.split()
        return len(file_as_words)

def get_book_chars(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        file_chars = list(file_contents)
        char_count = {}
        for char in file_chars:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count

def sort_on(dict):
    return dict["num"]

def sorted_list(dict):
    sorted_list_dict = []
    for char in dict:
        cur_dict = {}
        cur_dict["char"] = char
        cur_dict["num"] = dict[char]
        sorted_list_dict.append(cur_dict)
    sorted_list_dict.sort(reverse=True, key=sort_on)
    return sorted_list_dict

        
