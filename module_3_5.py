def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    print(first)
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    if first == 0:
        return 1
    else:
        return first


print(get_multiplied_digits(302151))
