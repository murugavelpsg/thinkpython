def fact(n):
    if not isinstance(n, int):
        print("Factorial is not valid for non-integers")
        return
    elif n < 0:
        print("Factorial is not implemented for negative numbers")
        return
    if n <= 0:
        return 1
    return n * fact(n-1)

def test_factorial():
    for i in range(1, 10):
        print("%d! = %d"% (i, fact(i)))
    for i in range(-2, 2):
        fact(i)
    fact("Hello World")

test_factorial()
