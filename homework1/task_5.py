from itertools import combinations_with_replacement as comb
from functools import reduce
from operator import mul


def count_find_num(primesL, limit):
    min_mul = reduce(mul, primesL)
    max_mul = min_mul
    count = 1
    i = 1 
    arr = []
    some_set = set()
    res = []
    if min_mul > limit:
        return res
    while i <= min_mul:
        arr = comb(primesL, i)
        for el in arr:
            some_set.add(reduce(mul, el) * min_mul)
        i += 1
    for el in some_set:
        if el <= limit:
            max_mul = max(el, max_mul)
            count +=1
    res.append(count)
    res.append(max_mul)
    return res

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []

