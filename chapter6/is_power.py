def is_power(a, b):
    if a == 0 or b == 0:
        return False
    elif b == 1:
        if a == 1:
            return True
        else:
            return False
    if a == 1 or (a/b == 1):
        return True
    is_divisible = a % b
    is_power_of_b = is_power(a//b, b)
    if a != 0 and is_divisible == 0 and is_power_of_b == True:
        return True
    else:
        return False

def test_is_power():
    print(is_power(25, 5))
    for i in range(1,5):
        for j in range(1, 5):
            print("is %d a power of %d? %s" % (i, j, is_power(i, j)))

test_is_power()
