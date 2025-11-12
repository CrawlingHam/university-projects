from re import escape, split

def tokenizer(text: str, delimiters: list[str], threshold: int = 3) -> list[str]:
    pattern: str = "|".join(map(escape, delimiters))
    words = split(pattern, text)

    result: list[str] = []

    for word in words:
        if len(word) > threshold:
            result.append(word)
    
    return result

if __name__ == "__main__":
    text = "Hello! This is a test. This is only a test. Testing 1, 2, 3."
    delimiters = [",", "!", ".", "?", " "]
    threshold = 3

    print(tokenizer(text, delimiters, threshold))
