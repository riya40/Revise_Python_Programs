def bubble_sort(array):
    for i in range(0, len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    print(array)


if __name__ == '__main__':
    size = int(input("enter the size elements"))
    list_elements = []
    len_ = int(input("enter the size to confirm "))
    for i in range(1, size):
        try:
            if len_ != size:
                raise Exception
            data = (input("enter the elements:"))
            list_elements.append(data)
            print(list_elements)
            print('bubble sort ordered elements:')
            bubble_sort(list_elements)
        except Exception as e:
            print("check the size for confirmation")
