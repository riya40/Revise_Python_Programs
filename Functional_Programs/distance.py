import math

"""
Calculating the Distance Between The Point By given Input 
"""


def calculating_distance(x_value, y_value):
    return math.sqrt((x_value * x_value) + (y_value * y_value))


if __name__ == '__main__':
    x_value = input("enter the value")
    y_value = input("enter the value")
    try:
        x_value = int(x_value)
        y_value = int(y_value)
        print(calculating_distance(x_value, y_value))
    except ValueError:
        raise ValueError("values should be numbers")