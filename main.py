from stats import word_count, char_count, dict_sort, sort_on

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    word_num = word_count(text)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------\nFound {word_num} total words\n--------- Character Count -------")
    for letter in dict_sort(char_count(text)):
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")

main()