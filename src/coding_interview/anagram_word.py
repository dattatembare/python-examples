from collections import Counter


def is_anagram(str1, str2):
    print(Counter(str1))  # Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})   Counter({'a': 2, 't': 2, 'D': 1})
    return Counter(str1) == Counter(str2)


print(is_anagram('abcd', 'dbca'))
print(is_anagram('Datta', 'dbca'))


def is_anagram_1(s1, s2):
    def sort(s):
        return sorted(s.lower().strip())

    return sort(s1) == sort(s2)


print(is_anagram_1('abcd', 'dbca'))
print(is_anagram_1('Datta', 'dbca'))


def is_anagram_dict(str1, str2):
    def char_dict(in_str):
        chars = {}
        for c in in_str.lower().strip()[::1]:
            if c in chars:
                chars[c] = chars.get(c) + 1
            else:
                chars[c] = 1
        return chars

    return char_dict(str1) == char_dict(str2)


print(is_anagram_dict('abcd', 'dbca'))
print(is_anagram_dict('Datta', 'Attad'))
print(is_anagram_dict('Datta', 'dbca'))

print(sorted('Datta'))  # ['D', 'a', 'a', 't', 't']
print(sorted('DaTta'))  # ['D', 'T', 'a', 'a', 't']
print(sorted('DaTta@186'))  # ['1', '6', '8', '@', 'D', 'T', 'a', 'a', 't']
print(sorted('Datta'.lower()))  # ['a', 'a', 'd', 't', 't']
