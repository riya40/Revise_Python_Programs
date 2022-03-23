import math


def calculating_values(a, b, c):
    root1 = -b + (math.sqrt(((b * b) - (4 * a * c)))) / 2 * a
    root2 = -b - (math.sqrt(((b * b) - (4 * a * c)))) / 2 * a
    return root1, root2


if __name__ == '__main__':
    a = input('enter value')
    b = input('enter value')
    c = input('enter value')
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        print(calculating_values(a, b, c))
    except ValueError:
        raise ValueError("enter the numbers only")