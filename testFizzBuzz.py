def bf(n):
    return 'fizzbuzz' if n % 15 == 0 else 'fizz' if n % 3 == 0 else 'buzz' if n % 5 == 0 else n


assert bf(1) == 1
assert bf(3) == 'fizz'
assert bf(5) == 'buzz'
assert bf(15) == 'fizzbuzz'
