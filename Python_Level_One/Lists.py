# LISTS

mylist = [1,2,3]
# mylist = ['asfd',1,2,3,3.4,454.6,'sdftgt',[1,2,3]]
print(mylist)

print(len(mylist))

# Indexing
print(mylist[-1])

# SLICING
print(mylist[2:])

# unlike strings, lists are mutable
mylist[0] = 'hello'


# METHODS

# To add certain element or a list as an element at the end of the list, use append
print("after appending the original list")
mylist.append('ef')
# mylist.append(['ed','fvrf','vf'])

# To extend the list i.e. to add list as a part of original list, use extend method
print("after extending the original list")
listtwo = ['df','fdv','fvde']
mylist.extend(listtwo)


# To remove an element from the list,
newlist = ['a','b','c','d','e']
item = newlist.pop(1)
# By default, pop method will remove the last Item
# pop method returns the element
print(newlist)
print(item)

# Reverse method happens in place i.e. the original list is changed, no need to reverse into another new list
newlist.reverse()
print("after reversing")
print(newlist)


# sorting
numberlist = [1,34,65,34,67,56,47,578]
numberlist.sort()
print(numberlist)


# Indexing a nested list
listfour = [1,2,['x','y','z']]
print(listfour[2][1])

# LIST COMPREHENSION
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)


# Lambda Expression

# filter

mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool,mylist)
print(list(evens))
