from stats import word_count, char_count, dict_sort
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    print(f"============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_num = word_count(text)
    print(f"Analyzing book found at {book_path}...\n----------- Word Count ----------\nFound {word_num} total words\n--------- Character Count -------")
    for letter in dict_sort(char_count(text)):
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")

main()