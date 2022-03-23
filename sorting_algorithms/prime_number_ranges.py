class Prime:
    """
    Printing The list Of Prime Numbers From 2 to 1000
    """
    def prime_number(self):
        prime_numbers = []
        for val in range(2, number + 1):
            if val < 2:
                continue
            if val == 2:
                prime_numbers.append(2)
                continue
            for x in range(2, val):
                if val % x == 0:
                    break
            else:
                prime_numbers.append(val)

        return prime_numbers


if __name__ == "__main__":
    pr = Prime()
    number = int(input("Enter Number upto what range u want 1000 "))
    try:
        if number == 1:
            raise Exception
        arr = pr.prime_number()
        print("Prime no are :", arr)
    except Exception as e:
        print(":", e)
