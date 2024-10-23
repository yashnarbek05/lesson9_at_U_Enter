import random


def is_anagram(str1, str2):
    if len(str1) != len(str1):
        return False
    return sorted(str1) == sorted(str2)

if __name__ == '__main__':
    print(is_anagram("aAb1aas","sbaA1"))
