from stats import count_words, count_chars, char_frequency_report

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text    

def main():
    filepath = 'books/frankenstein.txt'
    text = get_book_text(filepath)
    word_count = count_words(text)
    char_count = count_chars(text)
    

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print(f'--------- Character Count -------')
    for d in char_frequency_report(char_count):
        print(f"{d['char']}: {d['num']}")
    print('============= END ===============')

    print('============ DEBUG ============')
    print(char_frequency_report(char_count))
    print('============= END ===============')

if __name__ == "__main__":
    main()