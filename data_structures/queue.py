"""
 Queue is a linear data structure that stores items in First In First Out (FIFO) manner.
 With a queue the least recently added item is removed first.
"""

class Queue:

    def enqueue(self):
        if len(queue) == size:
            print("shouls maintain max balance")
        else:
            amount = input("enter the")
            queue.append(amount)
            print(amount, "is added")

    def dequeue(self):
        if not queue:
            print("you shuld main minimum ")
        else:
            elements = queue.pop(0)
            print("the pop element are:", elements)
            print(elements)


if __name__ == '__main__':
    size = int(input("enter the size of the stack:"))
    queue = []
    queueobject = Queue()
    while True:
        print("select operation\n 1.push element\n 2.pop element\n 3.exit")
        operation = int(input("select:"))
        if operation == 1:
            queueobject.enqueue()
        elif operation == 2:
            queueobject.dequeue()
        elif operation == 3:
            break
        else:
            print("select operation")