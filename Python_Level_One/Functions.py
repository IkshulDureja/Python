# Python uses snake case while javascript uses camel case while defining a function

def my_func(param1 = "default"):
    """
    THIS IS THE DOCSTRING
    """
    print("My first Python function {}".format(param1))

my_func()

# Printing within a funcion vs returning an Object
def hello():
    return "hello"

x = hello()
print(x)

def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+ num2
    else:
        return "Sorry, I need integers!"
result = addNum(2,3)
print(result)

# to check for type using the type keyword
print(type(result))


# Lambda Expression or anonymous function
# We use it when we have to only use the function once and that too inside of another function
# filter

myList = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0
# Lambda expression of even_bool function
lambda num : num%2 == 0
evens = filter(lambda num : num%2 == 0, myList)
print(list(evens))

# Some useful examples
st = "Hello"
st.lower()
st.upper()
st.split()

tweet = "Go Sports! #Sports"
hashtag = tweet.split("#")[1]
print(hashtag)

# in Operator
print( 'x' in [1,2,3,'x'])
