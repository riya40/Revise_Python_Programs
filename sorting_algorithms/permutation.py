class Permutation:
    """
    In this function the string that can permutes the all possible combinations
    in this the given input string shows all permutations
    eg:[a, b, c]= [b,c,a],[c,a,b],[a,c,b]
    """
    def string_permute(_list, f=0):
        if f >= len(_list):
            print(_list)
            return
        for s in range(f, len(_list)):
            _list[f], _list[s] = _list[s], _list[f]
            Permutation.string_permute(_list, f + 1)
            _list[f], _list[s] = _list[s], _list[f]


if __name__ == '__main__':
    _list = []
    size = int(input("enter the size elements"))
    len_ = int(input("enter the size to confirm "))
    for i in range(size):
        try:
            if len_ != size:
                raise Exception
            data = (input("enter the elements:"))
            _list.append(data)
            print(_list)
            Permutation.string_permute(_list)
        except Exception as e:
            print("check the size to perform the permutation", e)

