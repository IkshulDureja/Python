# STRINGS

# BASICS
"hello"
'hello'

" I'm a dog "

# Indexing
mystring = 'abcdefg'

# BEGINNING OF THE SLICE
# print(mystring[0])
# print(mystring[-1])
#
# # SLICING
# print(mystring[2:])
# # string from index 2
#
#
# print(mystring[4:])
# # string from index 4


# END OF THE SLICE
# # print(mystring[:3])
# # string upto but not including the index 3
#
#
# # print(mystring[2:5])
# # string from index 2 upto but not including index 5
#
#
# # STEP SIZE
#
# print(mystring)
# # grabs the entire string
#
# print(mystring[:])
# # grabs the entire string
#
#
# print(mystring[::])
# # grabs the entire string
#
#
# print(mystring[::1])
# # grabs the entire string
#
# print(mystring[::2])
# # step size of 2
#
#
# # you can redefine the complete string
# # but a string is immutable that means
# # that you can not override a particular element of the string



# BASIC METHODS

# # UPPER AND LOWER
# x=mystring.upper()
# print(x)
#
# y=mystring.lower()
# print(y)
#
# z=mystring.capitalize()
# print(z)
#
# a=mystring.split()
# # print(a)
#
#
# hellostring="Hello World"
#
# b=hellostring.split()
# print(b)
#
# c=hellostring.split('o')
# print(c)


# PRINT FROMATTING

x="Insert string here : {}".format("INSERT ME!")
print(x)

y="Item one:{} Item two:{}".format("dog","cat")
print(y)

z="Item one:{x} Item two:{y}".format(x="dog",y="cat")
print(z)


m="Item one:{y} Item two:{x}".format(x="dog",y="cat")
print(m)


n="Item one:{x} Item two:{x}".format(x="dog",y="cat")
print(n)
