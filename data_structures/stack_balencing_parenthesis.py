class Parenthesis_Balencing:
    def balencing(expression):

        list1 = ["[", "{", "("]
        parenthesis = {'}': '{', ']': '[', ')': '('}
        stack = []
        for i in expression:
            if i in list1:
                stack.append(i)
            elif len(stack) == 0 or parenthesis[i] != stack.pop():
                return False
        if stack:
            return False
        return True


if __name__ == '__main__':
    expression = '{{[]}}'
    print(f'{expression} is balenced:{Parenthesis_Balencing.balencing(expression)}')
