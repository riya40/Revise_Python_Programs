def calculating_chill(t, v):
    """
    Calculating The WindChill By using The Given Input
    By using the formula windchill = 35.74 + 0.6215 * t +(0.4275 * t -35.75) * v**0.16)
    t is temperature and v is wind speeed
    """
    windchill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
    return windchill


if __name__ == '__main__':
    try:
        t = float(input('enter value'))
        v = float(input('enter value'))
        print(calculating_chill(t, v))
    except ValueError:
        raise ValueError("values should not be numbers")