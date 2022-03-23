def mergeSort(array):
    if len(array) > 1:
        midvalue = len(array) // 2
        leftvalues = array[:midvalue]
        rightvalue = array[midvalue:]
        mergeSort(leftvalues)
        mergeSort(rightvalue)
        i = j = k = 0
        while i < len(leftvalues) and j < len(rightvalue):
            if leftvalues[i] < rightvalue[j]:
                array[k] = leftvalues[i]
                i += 1
            else:
                array[k] = rightvalue[j]
                j += 1
            k += 1
        while i < len(leftvalues):
            array[k] = leftvalues[i]
            i += 1
            k += 1

        while j < len(rightvalue):
            array[k] = rightvalue[j]
            j += 1
            k += 1


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == '__main__':
    size = int(input("enter the size elements to store"))
    array_elements = []
    len_ = int(input("enter the size to confirm "))
    for i in range(size):
        try:
            if len_ != size:
                raise Exception
            data = (input("enter the elements:"))
            array_elements.append(data)
            mergeSort(array_elements)
            print('merge sort ordered elements:')
            printList(array_elements)
        except Exception as e:
            print("check the size for confirmation")