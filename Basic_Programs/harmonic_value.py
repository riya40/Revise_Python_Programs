class Error(Exception):
    pass


class InputShouldNotZero(Error):
    pass


def harmonic_vale(num_, _num2):
    """
    Printing The Harmonic Value From the Given Range
    """
    try:
        if num_ == 0 and num2 == 0:
            raise InputShouldNotZero
        result = 0
        for i in range(num_, _num2):
            _result = (1/i)
            result = (result + (1 / i))
            print("ranges from:{} to {} the {} harmonic values:{}".format(num_, num2, i, _result))
        print("the entire value:{}".format(result))
    except InputShouldNotZero:
        print("input should be more than zero")


if __name__ == '__main__':
    num1 = int(input("enter the number"))
    num2 = int(input("enter the number"))
    harmonic_vale(num1, num2)
