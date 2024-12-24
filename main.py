def count_words(text: str) -> int:
    return len(text.split())


def character_count(text: str) -> dict:
    character_count = dict()
    lowercase_content = text.lower()
    character_count['a'] = lowercase_content.count('a')
    character_count['b'] = lowercase_content.count('b')
    character_count['c'] = lowercase_content.count('c')
    character_count['d'] = lowercase_content.count('d')
    character_count['e'] = lowercase_content.count('e')
    character_count['f'] = lowercase_content.count('f')
    character_count['g'] = lowercase_content.count('g')
    character_count['h'] = lowercase_content.count('h')
    character_count['i'] = lowercase_content.count('i')
    character_count['j'] = lowercase_content.count('j')
    character_count['k'] = lowercase_content.count('k')
    character_count['l'] = lowercase_content.count('l')
    character_count['m'] = lowercase_content.count('m')
    character_count['n'] = lowercase_content.count('n')
    character_count['o'] = lowercase_content.count('o')
    character_count['p'] = lowercase_content.count('p')
    character_count['q'] = lowercase_content.count('q')
    character_count['r'] = lowercase_content.count('r')
    character_count['s'] = lowercase_content.count('s')
    character_count['t'] = lowercase_content.count('t')
    character_count['u'] = lowercase_content.count('u')
    character_count['v'] = lowercase_content.count('v')
    character_count['w'] = lowercase_content.count('w')
    character_count['x'] = lowercase_content.count('x')
    character_count['y'] = lowercase_content.count('y')
    character_count['z'] = lowercase_content.count('z')
    return character_count


with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

print(count_words(file_contents))
