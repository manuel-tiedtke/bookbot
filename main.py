import sys
from stats import count_words, count_chars, char_frequency_report

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text    

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = count_words(text)
    char_count = count_chars(text)
    

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print(f'--------- Character Count -------')
    for d in char_frequency_report(char_count):
        char = d['char']
        display_char = char if char.isprintable() else char.encode('unicode_escape').decode('ascii')
        print(f"{display_char}: {d['num']}")
    print('============= END ===============')

if __name__ == "__main__":
    main()