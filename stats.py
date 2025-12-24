def word_count(text: str) -> int:
    words = text.split()
    return len(words)

def char_count(text: str) -> dict:
    text =text.lower()
    char_dict = {}
    for char in text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items['num']

def dict_sort(char_dict: dict) -> list:
    char_list = [{'char': k, 'num': v} for k, v in char_dict.items()]
    char_list.sort(key=sort_on, reverse=True)
    return char_list
    