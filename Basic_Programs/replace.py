def replace_name(input_string_, user_input_, replace_):
    """
    Taking The Input String From User
    Replace The Template By Using The User_input
    :param replace_: Generates the replace String
    :param user_input_: Predefined String
    :type input_string_: String that given by user
    """
    result = input_string_.replace(user_input_, replace_)
    return result


if __name__ == '__main__':
    try:
        input_string = input("enter the input:")
        user_input = input("enter which need to be replace:")
        replace_input = input("enter input for replace:")
        if len(user_input) < 3:
            raise ValueError
        print(replace_name(input_string, user_input, replace_input))
    except ValueError:
        print("enter userinput morethan 3")

