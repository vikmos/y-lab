from itertools import combinations_with_replacement as comb
from functools import reduce
from operator import mul


primesL = [2, 3]
limit = 200
min_mul = reduce(mul, primesL)
max_mul = min_mul
count = 1
i = min_mul
arr = []
some_set = set()
res = []
#if min_mul > limit:
#    return res
while i >= 1:
    #arr = comb(primesL, i)
    arr = comb(primesL, i)
    for el in arr:
        some_set.add(reduce(mul, el) * min_mul)
    i -= 1
print(some_set)
for el in some_set:
    if el <= limit:
        max_mul = max(el, max_mul)
        count +=1

res.append(count)
res.append(max_mul)
print(res)
