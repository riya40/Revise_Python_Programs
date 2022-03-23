class Error(Exception):
    pass


class RangeShouldNotExceed(Error):
    pass


def find_Triplets(arr, num):
    for i in range(0, num - 2):
        for j in range(i + 1, num - 1):
            for k in range(j + 1, num):
                if arr[i] + arr[j] + arr[k] == 0:
                    return arr[i], arr[j], arr[k]


if __name__ == '__main__':
    try:
        arr = list(map(int, input("Enter the array Elements:").split()))
        num = len(arr)
        if arr != num:
            raise RangeShouldNotExceed
        print(find_Triplets(arr, num))
    except RangeShouldNotExceed:
        print("RangeShouldNotExceed")