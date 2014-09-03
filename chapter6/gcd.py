def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    a = b
    return gcd(a, r)

def test_gcd():
    print(gcd(12, 8))
    print(gcd(10, 8))

test_gcd()
