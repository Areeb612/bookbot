from stats import number_of_words, get_characters, generate_report
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = (sys.argv[1])
    text = get_book_text(filepath)
    characters = get_characters(text)
    generate_report(filepath, text, characters)
    
    return 0


def get_book_text(filepath):
    with open(filepath, 'r') as file:
        file_contents = file.read()
    return file_contents

    
main()