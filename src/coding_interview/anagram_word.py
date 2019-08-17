from collections import Counter


def is_anagram(str1, str2):
    print(Counter(str1))  # Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})   Counter({'a': 2, 't': 2, 'D': 1})
    return Counter(str1) == Counter(str2)


print(is_anagram('abcd', 'dbca'))
print(is_anagram('Datta', 'dbca'))
