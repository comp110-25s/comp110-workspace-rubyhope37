def fizzbuzz(n: int) -> str:
    """An Adaptation of fizzbuzz"""
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(str(n))

    return fizzbuzz(n + 1)


print(fizzbuzz(1))
