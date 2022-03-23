class Sorting:
    """
    In this read we perform the binary search for the given list and found the element
    In this the list is divided based on mid value then it evaluates according to mid value to move forward or backward
    """
    def binary_search(self, list_elements, value):
        low_bound = 0
        upper_bound = len(list_elements)-1

        while low_bound <= upper_bound:
            md = (low_bound+upper_bound)//2
            if list_elements[md] == value:
                print("the searched value:", value, "at position:", md)
                return True
            else:
                if list_elements[md] < value:
                    low_bound = md+1
                else:
                    upper_bound = md-1
        return False


if __name__ == '__main__':
    sort = Sorting()
    list_elements = []
    size = int(input("enter the size elements"))
    for i in range(size):
        data = (input("enter the elements:"))
        list_elements.append(data)
    print(list_elements)
    value = (input("enter the value to search"))
    try:
        if sort.binary_search(list_elements, value):
            print("found")
            print(f'({type(list_elements).__name__}) {list_elements}')
        raise Exception
    except Exception as e:
        print("the entered element is not found please check entered number", e)
