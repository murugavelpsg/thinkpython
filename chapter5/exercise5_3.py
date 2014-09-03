def check_fermet(a, b, c, n):
    if a < 0 or b < 0:
        print("Either a or b is negative")
        return
    cn = pow(c, n)
    an_bn = pow(a, n) + pow(b, n)
    if n > 2 and an_bn == cn:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

def test_fermet():
    n = 3
    for i in range(1,5):
        for j in range(1, 5):
            for k in range(1, 5):
                check_fermet(i, j, k, n)

def test_fermet_with_input():
    a = input("Enter value of a: ")
    b = input("Enter value of b: ")
    c = input("Enter value of c: ")
    n = input("Enter value of n: ")
    check_fermet(int(a), int(b), int(c), int(n))

test_fermet_with_input()
