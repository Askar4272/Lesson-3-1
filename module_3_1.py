calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    str(string)
    a = len(string),string.upper(),string.lower()
    b = tuple(a)
    return (b)

def is_contains(string, list_to_search):
    count_calls()
    string_1 = str(string).lower()
    list(list_to_search)
    list_to_search_1 = [x.lower() for x in list_to_search]
    for j in range(len(list_to_search_1)):
        if string_1 == list_to_search_1[j]:
            pass
        elif string_1 != list_to_search_1[j] and j == len(list_to_search_1)-1:
            pass
    return string_1 == list_to_search_1[j]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)