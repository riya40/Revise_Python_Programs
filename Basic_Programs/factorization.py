class Error(Exception):
    pass


class InputShouldBeMoreThanOne(Error):
    pass


def prime_factors(_number):
    """
    Printing the Prime factors from given input number
    """
    factors = []  # to store the list factors list
    divisor = 2
    while _number % divisor == 0:  # checking the number can divisible with 2
        factors.append(divisor)  # adding the divisor to list
        _number = _number / 2
        divisor = divisor + 1
    while _number != 1 and divisor <= _number:
        if _number % divisor == 0:
            factors.append(divisor)
            _number /= divisor
        else:
            divisor += 2

    print("the prime factors are:")
    for i in range(len(factors)):
        print(factors[i])


if __name__ == '__main__':
    number = int(input("enter the number:"))
    try:
        if number < 2:
            raise InputShouldBeMoreThanOne
        prime_factors(number)
    except InputShouldBeMoreThanOne:
        print("input should give more than one")