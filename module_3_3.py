def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [35, 'botle', False]
values_dict = {'a': 12, 'b': 'mole', 'c': True}
values_list_2 = [54.42, "строка"]

print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
