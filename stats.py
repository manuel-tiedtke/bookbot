def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_chars(text: str) -> dict:
    char_count = {}
    for char in text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def char_frequency_report(char_count: dict) -> list:
    char_dicts = [{"char": k, "num": v} for k,v in char_count.items()]
    char_dicts.sort(reverse=True, key=lambda d: d['num'])
    return char_dicts
