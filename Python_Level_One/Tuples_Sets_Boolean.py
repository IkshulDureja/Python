#Booleans
True
False
0
1

# Tuples
# Tuples are immutable sequences
t = (1,2,3)
print(t[0])

tup = ('a',True,123)
print(tup[2])

# tup[2] = 'NEW'  ERROR beacuse tuples and strings are immutable

# SETS
# unordered collection of unique elements

x = set()

x.add(1)
x.add(2)
x.add(0.1)
x.add(4)
x.add(4)
x.add(4)
print(x)
# can print out in any way possible
# print out 4 only once because it only takes in unique elements
# once an element is already in set, you can not keep adding it multiple times

# which makes set call really convenient to call on a list of multiple elements
converted = set([1,1,2,2,3,3,3,3])
print(converted)
