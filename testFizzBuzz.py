def bf(n):
    if n % 15 == 0:
        return 'fizzbuzz'
    if n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'
    return n


assert bf(1) == 1
assert bf(3) == 'fizz'
assert bf(5) == 'buzz'
assert bf(15) == 'fizzbuzz'
