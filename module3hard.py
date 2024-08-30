data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    'Hello',
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    summa = 0

    # for item in data_structure:
    if isinstance(data, int):
        summa += data
    elif isinstance(data, str):
        summa += len(data)
    elif isinstance(data, (list, tuple, set)):
        for i in data:
            summa += calculate_structure_sum(i)
    elif isinstance(data, dict):
        data = [*data.items()]
        summa += calculate_structure_sum(data)

    return summa


result = calculate_structure_sum(data_structure)
print(result)
