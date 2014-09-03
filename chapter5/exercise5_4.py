def is_triangle(a, b, c):
    print(a, b, c)
    if a+b < c or b+c < a or c+a < b:
        print("No")
    else:
        print("Yes")

def test_triangle():
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                is_triangle(i, j, k)

test_triangle()
