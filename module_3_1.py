# Задача" Счётчик вызовов функций"

calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    length = len(string)
    a = (length, string.upper(), string.lower())
    return a


print(string_info('Banana'))
count_calls()
print(string_info('Library'))
count_calls()


def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = [s.lower() for s in list_to_search]
    if string in list_to_search:
        a = True
    else:
        a = False
    return a


print(is_contains('Urban', ['ban', 'BaNAN', 'urBAN']))
count_calls()
print(is_contains('cycle', ['recycle,cyclic']))
count_calls()
print(calls)
