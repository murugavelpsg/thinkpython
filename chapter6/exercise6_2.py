import math
def myHypotenuse(a, b):
    asquared = a**2
    bsquared = b**2
    return math.sqrt(asquared + bsquared)

def test_hypotenuse():
    c = myHypotenuse(3, 4)
    print(c)

test_hypotenuse()
