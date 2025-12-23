def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def word_count(text: str) -> int:
    words = text.split()
    return len(words)

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    word_num = word_count(text)
    print(f"Found {word_num} total words")

main()