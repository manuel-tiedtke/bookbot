def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_chars(text: str) -> dict:
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def char_frequency_report(char_count: dict) -> list:
    char_dicts = [{"char": k, "num": v} for k,v in char_count.items()]
    char_dicts.sort(reverse=True, key=lambda d: d['num'])
    return char_dicts

# Ignore this function, it's just my external memory and playground
def dojo():
    t = "Hello Python!"
    # Dict comprehension with symbols as key and the number of their occurrence as value. All casted to lower case. 
    cc = {c: t.count(c) for c in set(t.lower())}
    dict(sorted(cc.items()))
    dl = [{k: v} for k,v in cc.items()]
    # char_count[char] = char_count.get(char, 0) + 1