# !dictionary/hashtable/Objects
person = {
    'first_name': 'Tejas',
    'last_name': 'sabunkar',
    'is_male': True
}
print(person)

# Another Syntax -> dict() function

person2 = dict(first_name='Shailesh', age=38)
print(person2)

# !Accessing the values in hashtable/dictionary
print(person2['first_name'])
print(person2['age'])
# print(person2['is_male']) # !KeyError: 'is_male'

print('_____')
# !To get all the values from the dictionary
for props_value in person.values():
    print(props_value)

print('_____')
# !To get all the keys from the dictionary
for props in person.keys():
    print(props)

print('_____')
# !To get all the keys & values from the dictionary
# *dict.items() -> returns a list of tuples
for props in person.items():
    print(props)

print('___or___')
for key, value in person.items():
    print(key, '::', value)

# !Check if the key exist in the dictionary
computer = {
    'name': 'lenovo legio y520',
    'cpu': 'core-i7',
    'ram': 16,
    'ssd': '128 GB',
    'hdd': '1 TB',
    'is_expandable': True
}
print('name' in computer)  # True
print('key' in computer)  # False
print('key' in computer.keys())  # False # you can check on keys() method
print(16 in computer)  # False

# !Check if the value exist in the dictionary
print(16 in computer.values())  # True

# !dictionary Methods
print('_____dictionary Methods____')

# clear() - remove all keys and values in the dictionary
computer.clear()
print(computer)

d = dict(a=1, b=2, c=3)
d1 = d.copy()
print(d1)
print(d1 == d)  # True
# print(d1 in d) # !TypeError: unhashable type: 'dict'
print(d1 is d)  # False ==> copy value only, not copy by address (shallow copy)

# fromkeys()- create key and value pairs from comma separated values
print({}.fromkeys('a', 'b'))  # {'a': 'b'}
print({}.fromkeys('a', [1, 2, 3]))  # {'a': [1, 2, 3]}
print({}.fromkeys(['a'], 'b'))  # {'a': 'b'}
print({}.fromkeys(['a'], 1))  # {'a': 1}

print({}.fromkeys(['name', 'email', 'phone'], None))  # Assigning keys with default values as None
# o/p - {'name': None, 'email': None, 'phone': None}
print({}.fromkeys([]))  # {}
print({}.fromkeys('phone', '9'))  # {'p': '9', 'h': '9', 'o': '9', 'n': '9', 'e': '9'}

# get() - retri
