def count_uppercase(s):
    count = 0
    for i in range(len(s)):
        if s[i].isupper():
            count += 1
    return count
def count_lowercase(s):
    count = 0
    for i in range(len(s)):
        if s[i].islower():
            count += 1
    return count
def count_numbers(s):
    count = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            count += 1
    return count
def count_special_char(s):
    count = 0
    for i in range(len(s)):
        if not s[i].isalnum() and not s[i].isspace():
            count += 1
    return count
def count_spaces(s):
    count = 0
    for i in range(len(s)):
        if s[i] == " ":
            count += 1
    return count
def count_vowels(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'i' or s[i] == 'u' or s[i] == 'o' or s[i] == 'e' or s[i] == 'A' or s[i] == 'I' or s[i] == 'U' or s[i] == 'E' or s[i] == 'O':
            count += 1
    return count
def count_consonants(s):
    count = 0
    for i in range(len(s)):
        if s[i].isalpha() and not count_vowels(s[i]):
            count += 1
    return count
