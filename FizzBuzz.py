def FB(n):
    r = "Fizz" if n % 3 == 0 else ''
    return r + "Buzz" if n % 5 == 0 else n if r == '' else r
