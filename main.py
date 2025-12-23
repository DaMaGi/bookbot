from stats import word_count, char_count

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    word_num = word_count(text)
    print(f"Found {word_num} total words")
    print(f"Character count: {char_count(text)}")

main()