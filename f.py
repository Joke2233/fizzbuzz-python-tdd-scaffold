def f(n):
    return 'fizzbuzz' if n % 15 == 0 else 'fizz' \
        if n % 3 == 0 else 'buzz' if n % 5 == 0 else n
