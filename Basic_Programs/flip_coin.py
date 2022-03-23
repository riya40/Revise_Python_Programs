import random


def flip_coin(_coin):
    """
    Determining the flip coin using Random Function
    """
    if _coin < 0.5:
        return ((_coin / 1) * 100), "tail"
    else:
        return ((_coin / 1) * 100), "head"


if __name__ == '__main__':
    coin = (random.uniform(0, 1))
    print(flip_coin(coin))
