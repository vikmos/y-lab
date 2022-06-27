""" Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке. """

from collections import Counter


def bananas(s: str)-> set:
    result = set()
    letters_dict = dict()
    CONST = "banana"
    #if s == CONST:
    #    return set()    
    #else:
    counter = Counter(s)
    for letter in s:
        letters_dict[letter] = counter[letter]
    
    return letters_dict

print(bananas("bbananana"))
print(bananas("banana"))

"""
assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a", "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a", "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
"""

