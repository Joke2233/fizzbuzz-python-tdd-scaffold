def FB(n):
    if n%3 == 0:
        if n%5 == 0:
            return "FizzBuzz"
        else:
            return "Fizz"
    elif n%5 == 0:
        return "Buzz"
    else:
        return n