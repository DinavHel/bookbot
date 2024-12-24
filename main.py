def count_words(text: str) -> int:
    return len(text.split())


def character_count(text: str) -> dict:
    character_count = list()
    lowercase_content = text.lower()
    character_count.append({"character": "a", "num": lowercase_content.count("a")})
    character_count.append({"character": "b", "num": lowercase_content.count("b")})
    character_count.append({"character": "c", "num": lowercase_content.count("c")})
    character_count.append({"character": "d", "num": lowercase_content.count("d")})
    character_count.append({"character": "e", "num": lowercase_content.count("e")})
    character_count.append({"character": "f", "num": lowercase_content.count("f")})
    character_count.append({"character": "g", "num": lowercase_content.count("g")})
    character_count.append({"character": "h", "num": lowercase_content.count("h")})
    character_count.append({"character": "i", "num": lowercase_content.count("i")})
    character_count.append({"character": "j", "num": lowercase_content.count("j")})
    character_count.append({"character": "k", "num": lowercase_content.count("k")})
    character_count.append({"character": "l", "num": lowercase_content.count("l")})
    character_count.append({"character": "m", "num": lowercase_content.count("m")})
    character_count.append({"character": "n", "num": lowercase_content.count("n")})
    character_count.append({"character": "o", "num": lowercase_content.count("o")})
    character_count.append({"character": "p", "num": lowercase_content.count("p")})
    character_count.append({"character": "q", "num": lowercase_content.count("q")})
    character_count.append({"character": "r", "num": lowercase_content.count("r")})
    character_count.append({"character": "s", "num": lowercase_content.count("s")})
    character_count.append({"character": "t", "num": lowercase_content.count("t")})
    character_count.append({"character": "u", "num": lowercase_content.count("u")})
    character_count.append({"character": "v", "num": lowercase_content.count("v")})
    character_count.append({"character": "w", "num": lowercase_content.count("w")})
    character_count.append({"character": "x", "num": lowercase_content.count("x")})
    character_count.append({"character": "y", "num": lowercase_content.count("y")})
    character_count.append({"character": "z", "num": lowercase_content.count("z")})
    character_count.sort(reverse=True, key=lambda dict: dict["num"])

    return character_count


def print_report(text: str) -> None:
    print(f"--- Begin report of books/frankenstein.txt ---\n{count_words(text)} words found in the document\n")

    count = character_count(text)
    for record in count:
        print(f"The {record["character"]} character was found {record["num"]} times")
    return


with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

print_report(file_contents)
