def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def test_fibonacci():
    for i in range(0, 10):
        print("%d fibonacci number is %d" %(i, fibonacci(i)))

test_fibonacci()
