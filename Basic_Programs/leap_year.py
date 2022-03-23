class Error(Exception):
    pass


class InputShouldBeFour(Error):
    pass


def leap_year(_year):
    """
    Determining the given Year is Leap Or Not
    """
    try:
        digits = len(str(year))
        if digits != 4:
            raise InputShouldBeFour

        if (_year % 400 == 0) or (_year % 100 != 0) and (_year % 4 == 0):
            print(_year, "leap year")
        else:
            print(_year, "not leap year")
    except InputShouldBeFour:
        print("tne entered year should be four digits")


if __name__ == '__main__':
    year = int(input("enter the year"))
    leap_year(year)
