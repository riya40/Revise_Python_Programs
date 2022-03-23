def insertion_sort(elements):
    """
    Reads the list of Strings given by user
    Shows the Sorted Manner using the Insertion sort
    """
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0:
            if key < elements[j]:
                elements[j + 1] = elements[j]
                elements[j] = key
                j = j - 1
            else:
                break
    print(elements)


if __name__ == '__main__':
    size = int(input("enter the size elements to store"))
    list_elements = []
    len_ = int(input("enter the size to confirm "))
    for i in range(size):
        try:
            if len_ != size:
                raise Exception
            data = (input("enter the elements:"))
            list_elements.append(data)
            print(list_elements)
            print('insertion sort ordered elements:')
            insertion_sort(list_elements)
        except Exception as e:
            print("check the size for confirmation")

