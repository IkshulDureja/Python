# CONTROL FLOW


# COMPARISON OPERATORS

# Greater than
1 > 2
# Less than
1 < 2
# Greater than or Equal to
1 >= 1
# Less than or Equal to
1 <= 4
# Equality
1 == 1
1 == "1"
'hi' == 'bye'
# Inequality
1 != 2

# LOGICAL OPERATORS

# AND
(1 > 2) and (2 < 3)

# OR
(1 > 2) or (2 < 3)

# Multiple logical operators
(1 == 2) or (2 == 3) or (4 == 4)

# If statement
if 1 < 2:
    print('Yep!')

if 1 < 2:
    print('yep!')


# If Else - Make sure to line up the else with the if statement to "connect" them

if 1 < 2:
    print('first')
else:
    print('last')


if 1 > 2:
    print('first')
else:
    print('last')


# elseif
if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')

# FOR LOOPS

seq = [1,2,3,4,5,6]

for item in seq:
    print(item)

for item in seq:
    print("Hello")

for jelly in seq:
    print(jelly)

d = {"Sam":1, "Dan":2, "Frank":3}
# Dictionaries don't retain any order, so if you are using for loops with dictionaries, don't count on it happening in order
for k in d:
    print(k)
    print(d[k])

# Some methods to use for loops with Dictionaries
# for k in d.values
# for k in d.keys


# tuples

mypairs = [(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item)

# Tuples unpacking of Python

for tup1,tup2 in mypairs:
    print(tup2)
    print(tup1)

# While LOOPS

i = 1

while i<5:
    print("i is : {}".format(i))
    i = i+1

# Range functions can quickly generate integers for you
# range does not have to store all the integers
# range has one number memory at a time, it knows how to generate into next number
# we use range functions when we just have to iterate through integers
range(5)

list(range(0,5))

list(range(0,20,2))

list(range(0,21,2))

range(0,100000)

for item in range(10):
    print(item)

# LIST COMPREHENSION

s = [1,2,3,4]

# out = []
# for num in s:
#     out.append(num**2)
# print(out)


out = [num**2 for num in s]
print(out)
