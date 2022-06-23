""" Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа. """

def zeros(n: int) -> int:
    """Count trailing zeros"""
    if (n < 0):
        return -1
    zero_count = 0
    while (n >= 5):
        n //= 5
        zero_count += n
    return zero_count

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

