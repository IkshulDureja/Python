s = "GLOBAL VARIABLE!"
def func():
    global s
    s=50
    print(s)
func()
print(s)


def fun1():
    mylocal = 10
    print(locals())
    # returns dictionary
    print(globals())
    print(globals()['s'])
fun1()


def hello(name="jose"):
    return "hello "+name
print(hello())
mynewgreet = hello
# assign label to a function, setting it equal to function itself but not what the function returns
print(mynewgreet())


def hello1(name="jose"):
    print("THE HELLO1() FUNCTION HAS BEEN RUN!")
    def greet():
        return "THIS STRING IS INSIDE GRRET()"
    def welcome():
        return "THIS STRING IS INSIDE WELCOME()!"
    # print(greet())
    # print(welcome())
    # print("END OF HELLO1()")

# returning function
    if name == "jose":
        return greet
        # return the entire function not just the call of the functions
    else:
        return welcome
x = hello1()
# exact same thing as x=greet as if it was happening inside the hello1 function
print(x())


# function as the arguments
def hello2():
    return "HI JOSE!"
def other(func):
    print("HELLO")
    print(func())
other(hello2)
# not passing what the hello2 function returns but passing the hello2 function instead




# DECORATORS
def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func

# def func_needs_decorator():
#     print("THIS FUNCTION IS IN NEED OF A DECORATOR!")
# func_needs_decorator = new_decorator(func_needs_decorator)

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")

func_needs_decorator()
