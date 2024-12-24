def count_words(text: str) -> int:
    return len(text.split())

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

print(count_words(file_contents))
