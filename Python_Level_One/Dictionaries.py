# DICTIONARIES

my_stuff = {'key1':123,'key2':'value2', 'key3' : {'123':[1,2,'GrabMe']}}
# print(my_stuff['key2'])
# print(my_stuff)
print(my_stuff['key3']['123'][2])

print(my_stuff['key3']['123'][2].upper())

food = {'breakfast':'eggs','lunch':'pizza'}
print(food['breakfast'])

# Reassigning key-value pair
food['breakfast'] = 'burger'
print(food['breakfast'])

# Adding a new key-value pair
food['dinner'] = 'buffet'
print(food)
